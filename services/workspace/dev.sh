#!/bin/bash
service="PROJECT"
mkdir -p logs
echo -e "\033]0;XISA | ${service}\007"
source ../.env
export PYTHONPATH=../../common/src:$PYTHONPATH
cd src
python3 project/main.py
