import uuid

from .. import AUTH_TOKEN, BASE_ACTION, BASE_URL
from . import HttpxClient


def test_tasks_post_and_list():

    tags = {"test-tag": uuid.uuid4().hex}
    content_type = "application/json"
    headers = {"Authorization": f"Bearer {AUTH_TOKEN}", "Content-Type": content_type, "Accept": content_type}
    payload = {
        "url": "https://google.com",
        "referer": "https://www.google.com/",
        "_tags": tags,
    }

    response = HttpxClient(headers=headers).post(url=f"{BASE_URL}/{BASE_ACTION}/tasks", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert data.get("_tags").get("test-tag") == tags.get("test-tag")

    # ===

    task_id = data.get("task_id")

    response2 = HttpxClient(headers=headers).get(url=f"{BASE_URL}/{BASE_ACTION}/tasks", json=payload)
    assert response2.status_code == 200

    task_id_count = 0
    for task_item in response2.json():
        this_task_id = task_item.get("task_id")
        if task_id == this_task_id:
            task_id_count += 1

    assert task_id_count == 1
