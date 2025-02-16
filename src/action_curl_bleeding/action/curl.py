import base64
from hashlib import sha256
from tempfile import NamedTemporaryFile
from typing import Optional

from threatpatrols_action.exceptions import ThreatPatrolsException
from threatpatrols_action.shared.lib.execute_command import ExecuteCommand, execute_command

from .. import action_models, config

TEMP_FILE_PREFIX = config.LOGGER_NAME.lower()
CURL_BINARY = "curl"


def curl_bleeding(
    url: str,
    referer: Optional[str] = None,
    user_agent: Optional[str] = None,
    proxy: Optional[str] = None,
) -> action_models.ActionResponse:

    if not url:
        raise ThreatPatrolsException("CurlImpersonate(): url not set in collect")

    content_mime = None
    content_encoding = None
    request_headers = {}
    response_headers = {}
    status_code = None
    log_messages = []
    redirects = []

    with NamedTemporaryFile(prefix=TEMP_FILE_PREFIX + "-") as temp_file:
        args = ["--silent", "-vvv", "--location", "--output", temp_file.name, "--request", "GET"]
        if proxy:
            args.append("--proxy")
            args.append(proxy)
        if referer:
            args.append("--referer")
            args.append(referer)
        if user_agent:
            args.append("--user-agent")
            args.append(user_agent)
        args.append(str(url))

        result = execute_command(ExecuteCommand(CURL_BINARY, args=args, timeout=15))
        with open(temp_file.name, "rb") as f:
            content = f.read()

    if result.returncode != 0:
        error_messages = [f"{CURL_BINARY} terminated with non-zero exit code."]
        if result.stderr:
            error_messages.append(result.stderr.decode("utf8"))
        return action_models.ActionResponse(url=url, error_messages=error_messages)

    for stdout in result.stdout.decode("utf8").replace("\r", "").split("\n"):

        # http status code
        if stdout.startswith("< HTTP/"):
            status_code = int(stdout.split(" ")[2])

        # request headers
        if stdout.startswith("> ") and ":" in stdout and len(stdout) > 3:
            stdout_split = stdout.split(":", maxsplit=1)
            header = stdout_split[0].strip().replace("> ", "")
            request_headers[header] = stdout_split[1].strip()

        # response headers
        elif stdout.startswith("< ") and ":" in stdout and len(stdout) > 3:
            stdout_split = stdout.split(":", maxsplit=1)
            header = stdout_split[0].strip().replace("< ", "")
            response_headers[header] = stdout_split[1].strip()
            if header.lower() == "content-type":
                content_mime, content_encoding = __extract_content_mime_encoding(response_headers[header])
            if header.lower() == "location":
                redirects.append(response_headers[header])

        # log messages
        elif stdout.startswith("* ") and len(stdout) > 3:
            stdout_split = stdout.split(" ", maxsplit=1)
            log_messages.append(stdout_split[1].strip())
            if "Issue another request to this URL" in stdout:
                response_headers = {}

    return action_models.ActionResponse(
        url=url,
        content_b64=base64.b64encode(content).decode("utf8"),
        content_mime=content_mime,
        content_encoding=content_encoding,
        content_length=len(content),
        content_sha256=sha256(content).hexdigest(),
        redirects=redirects,
        request_headers=request_headers,
        response_headers=response_headers,
        status_code=status_code,
        log_messages=log_messages,
    )


def __extract_content_mime_encoding(content_type_header_value: str):
    content_encoding = None
    content_type_split = content_type_header_value.replace(" ", "").split(";")
    content_mime = content_type_split[0]
    if len(content_type_split) > 1 and "charset" in content_type_split[1].lower():
        charset_split = content_type_split[1].split("=")
        if len(charset_split) > 1:
            content_encoding = charset_split[1]
    return content_mime, content_encoding
