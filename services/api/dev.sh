#!/bin/bash
service="API"
echo -e "\033]0;XISA | ${service}\007"
mkdir -p logs
mkdir -p data/videos
mkdir -p data/detectors
source ../.env
export PYTHONPATH=../common/src:$PYTHONPATH
echo "Starting dev ${service} server in port ${API_PORT}"
fastapi dev src/api/main.py --port ${API_PORT} --host ${API_HOST}