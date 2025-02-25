import os
import subprocess
import time
from pathlib import Path

import pytest

from . import SERVER_PORT


@pytest.fixture(scope="session", autouse=True)
def api_server():
    apiserver_proc = subprocess.Popen(
        [
            "uvicorn",
            "--reload",
            "--log-level",
            "debug",
            "--proxy-headers",
            "--host",
            "0.0.0.0",
            "--port",
            f"{SERVER_PORT}",
            "action_curl_bleeding.api:entrypoint",
        ],
        env={"TPAS_DEBUG": "yes", "TPAS_CONFIG_FILE": "config.yml", "PATH": os.getenv("PATH")},
        cwd=str(Path(__file__).parent.parent.parent / "src"),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    # Give the server time to start
    time.sleep(5)

    # Check it started successfully
    assert not apiserver_proc.poll(), apiserver_proc.stdout.read().decode("utf-8")

    # yield to run pytests
    yield apiserver_proc

    # Shut it down at the end of the pytest session
    apiserver_proc.terminate()
