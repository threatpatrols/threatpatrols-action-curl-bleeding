import uuid

from .. import BASE_ACTION, BASE_URL
from . import HttpxClient


def test_calls_no_auth_calls_post():

    payload = {
        "url": "https://google.com",
        "referer": "https://www.google.com/",
        "tags": {"nonce-value": uuid.uuid4().hex},
        "headers": {"Content-Type": "application/json", "Accept": "application/json"},
    }

    response = HttpxClient().post(url=f"{BASE_URL}/{BASE_ACTION}/calls", data=payload)
    assert response.status_code == 403


def test_calls_bad_auth_calls_get():

    bad_auth_token = f"{uuid.uuid4().hex[0:12]}.{uuid.uuid4().hex[0:32]}"

    payload = {
        "headers": {
            "Authorization": f"Bearer {bad_auth_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
    }

    response = HttpxClient().get(url=f"{BASE_URL}/{BASE_ACTION}/calls", data=payload)
    assert response.status_code == 403


def test_calls_bad_auth_calls_post():

    bad_auth_token = f"{uuid.uuid4().hex[0:12]}.{uuid.uuid4().hex[0:32]}"

    payload = {
        "url": "https://google.com",
        "referer": "https://www.google.com/",
        "tags": {"nonce-value": uuid.uuid4().hex},
        "headers": {
            "Authorization": f"Bearer {bad_auth_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    }

    response = HttpxClient().post(url=f"{BASE_URL}/{BASE_ACTION}/calls", data=payload)
    assert response.status_code == 403
