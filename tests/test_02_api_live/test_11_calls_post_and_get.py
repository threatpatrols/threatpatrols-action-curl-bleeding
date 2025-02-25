import uuid

from .. import BASE_ACTION
from . import AUTH_TOKEN, BASE_URL, HttpxClient


def test_calls_post_and_get():

    tags = {"test-tag": uuid.uuid4().hex}
    content_type = "application/json"
    api_headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Content-Type": content_type,
        "Accept": content_type,
    }
    payload = {
        "url": "https://google.com",
        "referer": "https://www.google.com/",
        "_tags": tags,
    }

    response = HttpxClient(headers=api_headers).post(url=f"{BASE_URL}/{BASE_ACTION}/calls", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert tags.get("test-tag") == data.get("_tags").get("test-tag")

    call_id = data.get("_tags", {}).get("call_id")

    # ===

    response2 = HttpxClient(headers=api_headers).get(url=f"{BASE_URL}/{BASE_ACTION}/calls/{call_id}")
    assert response2.status_code == 200

    data2 = response2.json()
    assert tags.get("test-tag") == data.get("_tags").get("test-tag") == data2.get("_tags").get("test-tag")

    assert response.content == response2.content
