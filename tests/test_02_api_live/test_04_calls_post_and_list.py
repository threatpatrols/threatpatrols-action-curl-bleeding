import uuid

from .. import AUTH_TOKEN, BASE_ACTION, BASE_URL
from . import HttpxClient


def test_calls_post_and_list():

    tags = {"nonce-test-tag": uuid.uuid4().hex}
    content_type = "application/json"
    headers = {"Authorization": f"Bearer {AUTH_TOKEN}", "Content-Type": content_type, "Accept": content_type}
    payload = {
        "url": "https://google.com",
        "referer": "https://www.google.com/",
        "tags": tags,
    }

    response = HttpxClient(headers=headers).post(url=f"{BASE_URL}/{BASE_ACTION}/calls", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert data.get("tags", {}).get("nonce-test-tag") == tags.get("nonce-test-tag")

    # ===

    call_id = data.get("tags", {}).get("call_id")

    response2 = HttpxClient(headers=headers).get(url=f"{BASE_URL}/{BASE_ACTION}/calls", json=payload)
    assert response2.status_code == 200

    call_id_count = 0
    for call_item in response2.json():
        this_call_id = call_item.get("tags").get("call_id")
        if call_id == this_call_id:
            call_id_count += 1

    assert call_id_count == 1
