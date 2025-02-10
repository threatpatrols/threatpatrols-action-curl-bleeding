#
#  Copyright (c) 2025 Threat Patrols Pty Ltd <contact@threatpatrols.com>
#  See LICENSE.md for terms
#

from fastapi import FastAPI

from threatpatrols_action.api import ActionRoutes, add_redirect_route
from threatpatrols_action.api.lib.openapi_schema import custom_openapi
from threatpatrols_action.api.middlewares import load_middlewares
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

# Load routes
action_routes = ActionRoutes(action=curl_bleeding)
app.include_router(action_routes.router)

# Load middleware
load_middlewares(app=app)

# Apply redirects
add_redirect_route(app, request_path="/", redirect_url="/docs", tags=["System"], summary="Redirect to docs.")

# Customize the OpenAPI schema
app.openapi_schema = custom_openapi(app)

if __name__ == "__main__":
    import uvicorn

    logger.info(f"Start {config.TITLE} v{config.VERSION}")
    uvicorn.run(app, host="0.0.0.0", port=11235)
