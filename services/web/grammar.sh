#!/bin/bash
service="WEB | GRAMMAR"
echo -e "\033]0;XISA | ${service}\007"
cp ../player/src/Grammar.g4 ./src/app/Grammar.g4
cd src
cd app
antlr4 -Dlanguage=TypeScript Grammar.g4 -o ./grammar -visitor -encoding utf-8
