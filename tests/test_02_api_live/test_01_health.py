from . import BASE_URL, HttpxClient


def test_health():

    response = HttpxClient().get(url=f"{BASE_URL}/health")
    assert response.status_code == 200

    data = response.json()
    assert data.get("cpu_usage_p") >= 0 <= 100
    assert data.get("memory_usage_p") >= 0 <= 100
    assert data.get("background_tasks") >= 0 < 10000
