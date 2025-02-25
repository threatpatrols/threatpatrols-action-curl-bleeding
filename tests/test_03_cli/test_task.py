import json

from . import exec_command


def test_task_list():

    stdout2, stderr2, rc2 = exec_command("tpas-curl-bleeding", args=["task-list"])
    assert rc2 == 0

    for task_item in json.loads(stdout2):
        assert "state" in task_item.keys()
        assert "task_id" in task_item.keys()
        assert "_tags" in task_item.keys()

        assert "call_id" in task_item.get("_tags")
        assert task_item.get("_tags").get("task_id") == task_item.get("task_id")


def test_task_list_expired():

    stdout1, stderr1, rc1 = exec_command("tpas-curl-bleeding", args=["task-list", "expired-purge"])
    assert rc1 == 0

    data1 = json.loads(stdout1)
    assert data1 == []

    stdout2, stderr2, rc2 = exec_command("tpas-curl-bleeding", args=["task-list", "expired"])
    assert rc2 == 0

    data2 = json.loads(stdout2)
    assert data2 == []
