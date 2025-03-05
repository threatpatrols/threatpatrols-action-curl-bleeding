#
# Copyright [2025] Threat Patrols Pty Ltd (https://www.threatpatrols.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

ACTION_REQUEST_EXAMPLE = """
{
  "url": "https://httpbin.org/anything",
  "referer": "https://www.google.com/",
  "user_agent": "ActionRequestCurlBleeding/0.0.0",
  "headers": {"Accept-Encoding": "gzip"},
  "proxy": "socks5://127.0.0.1:1080",
  "_tags": {"foo": "bar"}
}
"""

ACTION_ITEM_SUMMARY_EXAMPLE = """
  {
    "url": "https://google.com",
    "content_length": 18604,
    "redirects": [ "https://www.google.com/" ],
    "status_code": 200,
    "_tags": {
      "action_name": "curl-bleeding",
      "api_key_id": "testing",
      "call_id": "20250216-1339-5142-5700-55fa0930637d",
      "request_id": "2218905dfb92477e-TPX"
    }
  }
"""

ACTION_ITEM_EXAMPLE = """
{
  "url": "https://google.com",
  "content_b64": "[truncated]",
  "content_mime": "text/html",
  "content_encoding": "ISO-8859-1",
  "content_length": 18573,
  "content_sha256": "bcb0e2615d74cc83949cd183afac7d19bb0f2778b342c4d6007803e69e171a31",
  "redirects": [
    "https://www.google.com/"
  ],
  "request_headers": {
    "Host": "www.google.com",
    "User-Agent": "ActionRequestCurlBleeding/0.0.0",
    "Accept": "*/*",
    "Referer": "https://www.google.com/"
  },
  "response_headers": {
    "date": "Sun, 16 Feb 2025 13:06:13 GMT",
    "expires": "-1",
    "cache-control": "private, max-age=0",
    "content-type": "text/html; charset=ISO-8859-1"
  },
  "status_code": 200,
  "log_messages": [
    "ALPN: curl offers h2,http/1.1",
    "TLSv1.3 (OUT), TLS handshake, Client hello (1):",
    "CAfile: /etc/ssl/certs/ca-certificates.crt",
    "CApath: /etc/ssl/certs",
    "TLSv1.3 (IN), TLS handshake, Server hello (2):",
    "TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):",
    "TLSv1.3 (IN), TLS handshake, Certificate (11):"
  ],
  "error_messages": null,
  "_tags": {
    "action_name": "curl-bleeding",
    "api_key_id": "testing",
    "call_id": "20250216-1306-1307-2400-329b4b6da303",
    "foo": "bar"
  }
}
"""
