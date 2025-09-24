#!/bin/bash

##
# Serve built Quartz content from docs/
##

cd $(dirname $0)/..
echo "Serving `pwd`/docs/ ..."

echo "Loading config..."
source config/local_config.sh

cd docs/
python ../bin/serve.py
