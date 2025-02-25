import random

from ..lib.client import HttpxClient

SERVER_PORT = random.randint(64000, 65000)
BASE_URL = f"http://127.0.0.1:{SERVER_PORT}"

AUTH_TOKEN_KEY = f"test{random.randint(100, 999)}"
AUTH_TOKEN_SECRET = f"testing-secret-{random.randint(10000000, 99999999)}-only"
AUTH_TOKEN = f"{AUTH_TOKEN_KEY}.{AUTH_TOKEN_SECRET}"
