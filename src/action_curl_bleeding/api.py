#
#  Copyright (c) 2025 Threat Patrols Pty Ltd <contact@threatpatrols.com>
#  See LICENSE.md for terms
#

from threatpatrols_action.api import load_api_app

from . import config
from .actions.curl import curl_bleeding

# Get the app
api_app = load_api_app(config=config, action=curl_bleeding)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(api_app, host="0.0.0.0", port=config.API_PORT)
