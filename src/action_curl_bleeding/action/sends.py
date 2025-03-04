from base64 import b64decode


def extract_content_b64(call_output, call_input):

    content_b64 = call_output.get("content_b64")
    if not content_b64:
        return None

    return b64decode(content_b64)


action_callback_sends_map = {"report": extract_content_b64}
