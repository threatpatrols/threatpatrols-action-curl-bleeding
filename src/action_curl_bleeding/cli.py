#
#  Copyright (c) 2025 Threat Patrols Pty Ltd <contact@threatpatrols.com>
#  See LICENSE.md for terms
#

from threatpatrols_action.cli import load_cli_app

from . import config
from .action.curl import curl_bleeding


def entrypoint():
    cli_app = load_cli_app(config=config, action=curl_bleeding)
    cli_app()
