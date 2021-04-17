#!/bin/zsh



# java -jar /usr/local/lib/antlr-4.8-complete.jar -no-listener -visitor -Dlanguage=Python3 *.g4 -o ../grammar
java -jar /usr/local/lib/antlr-4.8-complete.jar -Dlanguage=Python3 *.g4 -o ../grammar