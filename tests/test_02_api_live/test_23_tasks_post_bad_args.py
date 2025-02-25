import uuid

from .. import BASE_ACTION
from . import AUTH_TOKEN, BASE_URL, HttpxClient


def test_tasks_post_no_tag():

    content_type = "application/json"
    headers = {"Authorization": f"Bearer {AUTH_TOKEN}", "Content-Type": content_type, "Accept": content_type}
    payload = {
        "url": "https://google.com",
        "referer": "https://www.google.com/",
    }

    response = HttpxClient(headers=headers).post(url=f"{BASE_URL}/{BASE_ACTION}/tasks", json=payload)
    assert response.status_code == 200


def test_tasks_post_bad_args():

    content_type = "application/json"
    headers = {"Authorization": f"Bearer {AUTH_TOKEN}", "Content-Type": content_type, "Accept": content_type}
    payload = {
        "url": "https://google.com",
        "referer": "https://www.google.com/",
        "xx-" + str(uuid.uuid4().hex): str(uuid.uuid4().hex),  # bad arg
        "_tags": {"foo": "bar"},
    }

    response = HttpxClient(headers=headers).post(url=f"{BASE_URL}/{BASE_ACTION}/tasks", json=payload)
    assert response.status_code == 200
