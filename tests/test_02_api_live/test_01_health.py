from .. import BASE_URL
from . import HttpxClient


def test_health():

    response = HttpxClient().get(url=f"{BASE_URL}/health")
    assert response.status_code == 200

    data = response.json()
    assert data.get("status") == "healthy"
    assert data.get("memory_usage") >= 0 <= 100
    assert data.get("cpu_usage") >= 0 <= 100
    assert data.get("background_tasks") >= 0 < 10000
