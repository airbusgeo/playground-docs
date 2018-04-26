#! /usr/bin/env bash

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

HOST="localhost"
PORT="8000"
TILE="data/tile.png"

WORKDIR="tmp"
REQUEST="$WORKDIR/request.json"

# create workdir
mkdir -p $WORKDIR

# create request
echo "Create request"

echo '{' > $REQUEST
echo '  "zoom": 16,' >> $REQUEST
echo '  "tile1Format": "image/png",' >> $REQUEST
echo -n '  "tile1": "' >> $REQUEST
cat $TILE | base64 >> $REQUEST
echo '",' >> $REQUEST
echo '  "tile2Format": "image/png",' >> $REQUEST
echo -n '  "tile2": "' >> $REQUEST
cat $TILE | base64 >> $REQUEST
echo '"' >> $REQUEST
echo '}' >> $REQUEST

# predict
echo "Launch prediction"

time curl -X POST http://$HOST:$PORT/api/jobs -d @$REQUEST --header "Content-Type: application/json" --header "X-Correlation-ID: 9876543210" --header "X-ADS-Debug: true"

# clean
rm -rf $WORKDIR
