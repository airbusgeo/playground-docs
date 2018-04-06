#! /usr/bin/env bash

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
echo '  "zoom": "16",' >> $REQUEST
echo '  "tileFormat": "image/png",' >> $REQUEST
echo -n '  "tile": "' >> $REQUEST
cat $TILE | base64 >> $REQUEST
echo '"' >> $REQUEST
echo '}' >> $REQUEST

# predict
echo "Launch prediction"

time curl -X POST http://$HOST:$PORT/api/jobs -d @$REQUEST --header "Content-Type: application/json" --header "X-Correlation-ID: 9876543210" --header "X-ADS-Debug: true"

# clean
rm -rf $WORKDIR
