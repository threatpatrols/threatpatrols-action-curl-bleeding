import json

from . import exec_command


def test_call():

    url = "https://google.com"

    stdout, stderr, rc = exec_command("tpas-curl-bleeding", args=["call", "--url", url])
    assert rc == 0
    assert "error" not in stderr.decode().lower()

    data = json.loads(stdout)
    assert data.get("status_code") == 200
    assert data.get("url") == url

    assert "_tags" in data.keys()
    assert "call_id" in data.get("_tags").keys()


def test_call_get():

    url = "https://google.com"

    stdout1, stderr1, rc1 = exec_command("tpas-curl-bleeding", args=["call", "--url", url])
    assert rc1 == 0
    assert "error" not in stderr1.decode().lower()

    data1 = json.loads(stdout1)
    assert data1.get("status_code") == 200
    assert data1.get("url") == url

    assert "_tags" in data1.keys()
    assert "call_id" in data1.get("_tags").keys()

    call_id = data1.get("_tags").get("call_id")

    stdout2, stderr2, rc2 = exec_command("tpas-curl-bleeding", args=["call-get", call_id])
    assert rc2 == 0

    assert stdout1 == stdout2


def test_call_list():

    url = "https://google.com"

    stdout1, stderr1, rc1 = exec_command("tpas-curl-bleeding", args=["call", "--url", url])
    assert rc1 == 0
    assert "error" not in stderr1.decode().lower()

    data1 = json.loads(stdout1)
    call_id = data1.get("_tags").get("call_id")

    stdout2, stderr2, rc2 = exec_command("tpas-curl-bleeding", args=["call-list"])
    assert rc2 == 0

    call_id_count = 0
    for call_item in json.loads(stdout2):
        this_call_id = call_item.get("_tags").get("call_id")
        if call_id == this_call_id:
            call_id_count += 1

    assert call_id_count == 1


def test_call_list_expired():

    stdout1, stderr1, rc1 = exec_command("tpas-curl-bleeding", args=["call-list", "expired-purge"])
    assert rc1 == 0

    data1 = json.loads(stdout1)
    assert data1 == []

    stdout2, stderr2, rc2 = exec_command("tpas-curl-bleeding", args=["call-list", "expired"])
    assert rc2 == 0

    data2 = json.loads(stdout2)
    assert data2 == []
