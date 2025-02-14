#
#  Copyright (c) 2025 Threat Patrols Pty Ltd <contact@threatpatrols.com>
#  See LICENSE.md for terms
#

__title__ = "Curl Bleeding Action"
__version__ = "0.1.0"

from threatpatrols_action import action_models, config

from .action.models import ActionListItemResponse, ActionRequest, ActionResponse

config.TITLE = __title__
config.VERSION = __version__
config.ACTION_NAME = "curl-bleeding"

action_models.ActionRequest = ActionRequest
action_models.ActionResponse = ActionResponse
action_models.ActionListItemResponse = ActionListItemResponse
