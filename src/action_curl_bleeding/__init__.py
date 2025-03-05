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

__title__ = "Curl Bleeding Action"
__version__ = "0.1.0"

from threatpatrols_action import action_models, config

from .action.models import ActionItemCurlBleeding, ActionItemSummaryCurlBleeding, ActionRequestCurlBleeding

config.TITLE = __title__
config.VERSION = __version__
config.ACTION_NAME = "curl-bleeding"

action_models.ActionRequest = ActionRequestCurlBleeding
action_models.ActionItem = ActionItemCurlBleeding
action_models.ActionItemSummary = ActionItemSummaryCurlBleeding
