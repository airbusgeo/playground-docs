# Copyright 2018 Airbus. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Playground API utils
"""

import os
import json
import jsonschema
from jsonschema import ValidationError


class APIHelper():
    def __init__(self):
        """
        Helper class for validating input and config schemas and for loading the describe data 
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))

        describe_template_path = os.path.join(
            dir_path, 'templates', 'tile-change-detection-describe.json')

        config_schema_path = os.path.join(dir_path, 'templates',
                                          'tile-change-detection-config.json')

        input_schema_path = os.path.join(dir_path, 'templates',
                                         'tile-change-detection-input.json')

        open_api_path = os.path.join(dir_path, 'templates',
                                     'api_geo_process_v1.0.yaml')

        with open(open_api_path, 'r') as f:
            self.open_api_data = f.read()

        with open(describe_template_path, 'r') as f:
            self.describe_data = json.loads(f.read())

        with open(input_schema_path, 'r ') as f:
            self.input_schema = json.loads(f.read())

        with open(config_schema_path, 'r ') as f:
            self.config_schema = json.loads(f.read())

    def load_process_data(self, process_data):
        """
        Loads the basic describe template and adds user-defined information 

        """
        self.describe_data.update(process_data)

        # TODO check if dict is correct
        for key in self.describe_data:
            if self.describe_data.get(key) is None:
                raise ValueError(
                    "Missing {} key value in process data".format(key))

        return self.describe_data

    def validate_input(self, input_data):
        """
        Validate an input json 
        """
        try:
            jsonschema.validate(input_data, self.input_schema)
        except ValidationError as e:
            raise ValidationError(e.message)

    def validate_config(self, config_data):
        """
        Validate a config json
        """
        try:
            jsonschema.validate(config_data, self.config_schema)
        except ValidationError as e:
            raise ValidationError(e.message)
