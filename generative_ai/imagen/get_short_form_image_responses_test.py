# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

import backoff

import get_short_form_image_responses

from google.api_core.exceptions import ResourceExhausted


_RESOURCES = os.path.join(os.path.dirname(__file__), "test_resources")
_PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
_LOCATION = "us-central1"
_INPUT_FILE = os.path.join(_RESOURCES, "cat.png")
_QUESTION = "What breed of cat is this a picture of?"


@backoff.on_exception(backoff.expo, ResourceExhausted, max_time=60)
def test_get_short_form_image_responses() -> None:
    response = get_short_form_image_responses.get_short_form_image_responses(
        _PROJECT_ID,
        _LOCATION,
        _INPUT_FILE,
        _QUESTION,
    )

    assert len(response) > 0 and "tabby" in response[0]
