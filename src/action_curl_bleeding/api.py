#
#  Copyright (c) 2025 Threat Patrols Pty Ltd <contact@threatpatrols.com>
#  See LICENSE.md for terms
#

from fastapi import FastAPI

from threatpatrols_action.api import ActionRoutes, load_fastapi_components
from threatpatrols_action.exceptions import generate_api_exception_response_handlers
from threatpatrols_action.shared.lib.logger_init import logger_get, logger_setlevel

from . import config
from .actions.curl import curl_bleeding

# Set the logger level early
logger = logger_get(name=config.LOGGER_NAME)
logger_setlevel(name=config.LOGGER_NAME, loglevel=config.LOGGER_LEVEL)

# Establish the FastAPI app instance
app = FastAPI(
    debug=config.DEBUG,
    version=config.VERSION,
    title=config.TITLE,
    docs_url=None,
    exception_handlers=generate_api_exception_response_handlers(),
)

# Load the action routes
action_routes = ActionRoutes(action=curl_bleeding)

# Load the remaining FastAPI components
load_fastapi_components(app=app, action_routes=action_routes)

if __name__ == "__main__":
    import uvicorn

    logger.info(f"Start {config.TITLE} v{config.VERSION}")
    uvicorn.run(app, host="0.0.0.0", port=11235)
