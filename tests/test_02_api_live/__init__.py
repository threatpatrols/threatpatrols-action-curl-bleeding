import random

from ..lib.client import HttpxClient

SERVER_PORT = random.randint(64000, 65000)
BASE_URL = f"http://127.0.0.1:{SERVER_PORT}"
AUTH_TOKEN = "internal-microservice.demo-secret-CHANGE-ME-PLEASE-alphanumeric"
