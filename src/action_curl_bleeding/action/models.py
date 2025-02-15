from typing import Optional

from pydantic import ConfigDict

from threatpatrols_action.shared.models import TagsBaseModel


class ActionRequestCurlBleeding(TagsBaseModel):

    url: str
    referer: Optional[str] = None
    user_agent: Optional[str] = None
    proxy: Optional[str] = None

    model_config = ConfigDict(
        extra="forbid",
        json_schema_extra={
            "example": {
                "url": "https://google.com",
                "referer": "https://www.google.com/",
                "user_agent": None,
                "proxy": None,
                "tags": {"foo": "bar"},
            }
        },
    )


class ActionResponseCurlBleeding(TagsBaseModel):
    url: Optional[str] = None

    content_b64: Optional[str] = None
    content_mime: Optional[str] = None
    content_encoding: Optional[str] = None
    content_length: Optional[int] = None
    content_sha256: Optional[str] = None

    redirects: Optional[list[str]] = None

    request_headers: Optional[dict] = None
    response_headers: Optional[dict] = None
    status_code: Optional[int] = None

    log_messages: Optional[list[str]] = None
    error_messages: Optional[list[str]] = None


class ActionListItemResponseCurlBleeding(TagsBaseModel):
    url: Optional[str] = None
    content_length: Optional[int] = None
    redirects: Optional[list[str]] = None
    status_code: Optional[int] = None
