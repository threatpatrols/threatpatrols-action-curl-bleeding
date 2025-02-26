import random

from ..lib.client import HttpxClient

DEVLOCAL = False  # Use developer local manually running api server
DEVLOCAL_KEY = "credential01example"  # see config.yml
DEVLOCAL_SECRET = "test-secret-CHANGE-ME-PLEASE-alphanumeric"  # see config.yml

# ===

SERVER_PORT = 11235 if DEVLOCAL else random.randint(64000, 65000)
BASE_URL = f"http://127.0.0.1:{SERVER_PORT}"

AUTH_TOKEN_KEY = DEVLOCAL_KEY if DEVLOCAL else f"test{random.randint(100, 999)}"
AUTH_TOKEN_SECRET = DEVLOCAL_SECRET if DEVLOCAL else f"testing-secret-{random.randint(10000000, 99999999)}-only"
AUTH_TOKEN = f"{AUTH_TOKEN_KEY}.{AUTH_TOKEN_SECRET}"
