#!/bin/bash
service="LANGAUGE"
mkdir -p logs
mkdir -p data
echo -e "\033]0;XISA | ${service}\007"
source ../.env
export PYTHONPATH=../../common/src:$PYTHONPATH
cd src
python3 language/main.py
