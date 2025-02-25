#
#  Copyright (c) 2025 Threat Patrols Pty Ltd <contact@threatpatrols.com>
#  See LICENSE.md for terms
#

from threatpatrols_action.api import load_api_app

from . import config
from .action.curl import curl_bleeding

entrypoint = load_api_app(config=config, action=curl_bleeding)
