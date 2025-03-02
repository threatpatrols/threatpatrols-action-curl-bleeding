from . import BASE_URL, HttpxClient


def test_health():

    response = HttpxClient().get(url=f"{BASE_URL}/health")
    assert response.status_code == 200

    data = response.json()
    assert data.get("cpu_usage_p") >= 0 <= 1
    assert data.get("memory_used_p") >= 0 <= 1
