import httpx


class HttpxClient:
    headers: dict
    request_timeout: int
    verify: bool
    debug: bool

    def __init__(self, headers: dict = None, request_timeout=10, verify: bool = True, debug: bool = False):
        self.headers = headers if headers else {}
        self.request_timeout = request_timeout
        self.verify = verify
        self.debug = debug

    @property
    def user_agent(self) -> str:
        return f"tpas-test/0.0.0"

    def get(self, **kwargs):
        return self.request(method="GET", **kwargs)

    def post(self, **kwargs):
        return self.request(method="POST", **kwargs)

    def patch(self, **kwargs):
        return self.request(method="PATCH", **kwargs)

    def request(self, **kwargs) -> httpx.Response:
        event_hooks = {"request": [], "response": []}

        if "params" in kwargs and isinstance(kwargs["params"], dict):
            kwargs["params"] = {k: v for (k, v) in kwargs["params"].items() if v or isinstance(v, int)}

        headers = {**{"User-Agent": self.user_agent}, **self.headers}

        httpx_client = {
            "headers": headers,
            "http2": False,
            "timeout": self.request_timeout,
            "trust_env": False,
            "verify": self.verify,
            "event_hooks": event_hooks,
        }

        if "url" not in kwargs:
            raise ValueError("Parameter 'url' for request() not present")

        with httpx.Client(**httpx_client) as client:
            request = client.build_request(**kwargs)
            return client.send(request=request)
