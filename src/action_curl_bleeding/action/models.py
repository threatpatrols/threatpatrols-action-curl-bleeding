import json
from typing import Optional

from pydantic import ConfigDict

from threatpatrols_action.shared.models import BaseModelPrivateHandler

from . import ACTION_ITEM_EXAMPLE, ACTION_LIST_ITEM_EXAMPLE, ACTION_REQUEST_EXAMPLE


class ActionRequestCurlBleeding(BaseModelPrivateHandler):

    url: str
    referer: Optional[str] = None
    user_agent: Optional[str] = None
    headers: Optional[dict[str, str]] = None
    proxy: Optional[str] = None

    model_config = ConfigDict(extra="allow", json_schema_extra={"example": json.loads(ACTION_REQUEST_EXAMPLE)})


class ActionItemCurlBleeding(BaseModelPrivateHandler):
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

    model_config = ConfigDict(extra="allow", json_schema_extra={"example": json.loads(ACTION_ITEM_EXAMPLE)})


class ActionListItemCurlBleeding(BaseModelPrivateHandler):
    url: Optional[str] = None
    content_length: Optional[int] = None
    redirects: Optional[list[str]] = None
    status_code: Optional[int] = None

    model_config = ConfigDict(extra="allow", json_schema_extra={"example": json.loads(ACTION_LIST_ITEM_EXAMPLE)})
