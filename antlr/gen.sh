#!/bin/zsh



# java -jar /usr/local/lib/antlr-4.8-complete.jar -no-listener -visitor -Dlanguage=Python3 *.g4 -o ../grammar
java -jar /usr/local/lib/antlr-4.9.3-complete.jar -Dlanguage=Python3 *.g4 -o ../grammar

# test file
java -jar /usr/local/lib/antlr-4.9.3-complete.jar -o ./.antlr

cd .antlr

javac *.java

java org.antlr.v4.gui.TestRig ObjectiveC translationUnit -gui '/Users/annidy/Work/bdp150/dist/project/TTMicroApp/Timor/Core/Common/BaseData/BDPCommonManager.m'
