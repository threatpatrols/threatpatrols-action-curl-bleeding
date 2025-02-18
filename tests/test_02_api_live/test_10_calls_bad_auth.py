import uuid

from hlid import HLID

from .. import BASE_ACTION, BASE_URL
from . import HttpxClient


def test_calls_bad_auth_calls_get():

    bad_auth_token = f"{uuid.uuid4().hex[0:12]}.{uuid.uuid4().hex[0:32]}"
    api_headers = {
        "Authorization": f"Bearer {bad_auth_token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    response = HttpxClient(headers=api_headers).get(url=f"{BASE_URL}/{BASE_ACTION}/calls")
    assert response.status_code == 403


def test_calls_bad_auth_calls_get_item():

    bad_auth_token = f"{uuid.uuid4().hex[0:12]}.{uuid.uuid4().hex[0:32]}"
    api_headers = {
        "Authorization": f"Bearer {bad_auth_token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    item_id = str(HLID())
    response = HttpxClient(headers=api_headers).get(url=f"{BASE_URL}/{BASE_ACTION}/calls/{item_id}")
    assert response.status_code == 403


def test_calls_no_auth_calls_post():

    api_headers = {"Content-Type": "application/json", "Accept": "application/json"}
    post_data = {
        "url": "https://google.com",
        "referer": "https://www.google.com/",
        "headers": {"Content-Type": "application/json", "Accept": "application/json"},
    }

    response = HttpxClient(headers=api_headers).post(url=f"{BASE_URL}/{BASE_ACTION}/calls", json=post_data)
    assert response.status_code == 403


def test_calls_bad_auth_calls_post():

    bad_auth_token = f"{uuid.uuid4().hex[0:12]}.{uuid.uuid4().hex[0:32]}"
    api_headers = {
        "Authorization": f"Bearer {bad_auth_token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    post_data = {
        "url": "https://google.com",
        "referer": "https://www.google.com/",
        "headers": {"Content-Type": "application/json", "Accept": "application/json"},
    }

    response = HttpxClient(headers=api_headers).post(url=f"{BASE_URL}/{BASE_ACTION}/calls", json=post_data)
    assert response.status_code == 403
