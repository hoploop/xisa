#!/bin/bash
service="PLAYER | GRAMMAR"
echo -e "\033]0;XISA | ${service}\007"
export PYTHONPATH=../../common/src:$PYTHONPATH
cd src
antlr4 -Dlanguage=Python3 Grammar.g4 -o ./player/grammar -visitor -encoding utf-8