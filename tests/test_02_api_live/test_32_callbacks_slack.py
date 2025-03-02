from .. import BASE_ACTION
from . import AUTH_TOKEN, BASE_URL, HttpxClient


def test_calls_post_w_slack_callbacks():

    callbacks = ["slack.slack01example"]
    content_type = "application/json"
    api_headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Content-Type": content_type,
        "Accept": content_type,
    }
    payload = {
        "url": "https://google.com",
        "referer": "https://www.google.com/",
        "_callbacks": callbacks,
    }

    response = HttpxClient(headers=api_headers).post(url=f"{BASE_URL}/{BASE_ACTION}/calls", json=payload)
    assert response.status_code == 200

    data = response.json()
    call_id = data.get("_tags", {}).get("call_id")
    assert call_id is not None


def test_tasks_w_slack_callbacks():

    callbacks = ["slack.slack01example"]
    content_type = "application/json"
    api_headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Content-Type": content_type,
        "Accept": content_type,
    }
    payload = {
        "url": "https://google.com",
        "referer": "https://www.google.com/",
        "_callbacks": callbacks,
    }

    response = HttpxClient(headers=api_headers).post(url=f"{BASE_URL}/{BASE_ACTION}/tasks", json=payload)
    assert response.status_code == 200

    data = response.json()
    task_id = data.get("_tags", {}).get("task_id")
    assert task_id is not None
