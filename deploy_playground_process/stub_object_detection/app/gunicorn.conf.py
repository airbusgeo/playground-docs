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

"""Gunicorn (http server) configuration.
"""

import multiprocessing

worker_class = 'sync'
# Note: You must configure your nb of workers accordingly with your model's requirements
# Usually ML models are "computation heavy" thus requires a low number of workers per instance
workers = 2 # default: multiprocessing.cpu_count() * 2 + 1
# timeout = 60
