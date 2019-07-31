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

# Create a container image from a stock Python 2.7 Debian image
FROM python:3.7-slim

# Install system dependencies: libgeos
RUN apt-get update && \
    apt-get install -qy libgeos-c1v5 build-essential && \
    apt-get clean

# update pip to avoid debian problems
RUN pip install -U --no-cache-dir pip

# Install application requirements
COPY requirements.txt /
RUN pip install -U --no-cache-dir -r requirements.txt

# Install application
COPY app /app/

# Set workdir
WORKDIR /app/

# Launch web application
EXPOSE 8080
ENTRYPOINT ["python", "app.py"]

