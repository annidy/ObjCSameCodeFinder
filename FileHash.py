# coding: utf-8


import sys
import os
import re
from objctoken.FileObject import FileObject, LineString
from objctoken.FuncImplToken import FuncImplToken
from objctoken.KeywordToken import ImplementToken, EndToken, CommentsToken
from Blamer import Blamer
from FuncHash import FuncHash
from enum import Enum, auto

class FuncState(Enum):
    TopLevel = 1
    Implement = 2

class FileHash:

    def __init__(self, path):
        self.blamer = Blamer(path)
        self.funcList = []
        self.path = path
        self.fileObject = FileObject(path)

        funcState = FuncState.TopLevel
        funcToken = None
        for line in self.fileObject:
            if funcState == FuncState.TopLevel:
                token = ImplementToken(line)
                if token.test():
                    funcState = FuncState.Implement
                    continue

            if funcState == FuncState.Implement:
                if funcToken == None:
                    token = FuncImplToken(line)
                    if token.test():
                        funcToken = token
                    else:
                        token = EndToken(line)
                        if token.test():
                           funcState = FuncState.TopLevel 
                           continue
                    
                if funcToken != None:
                    funcToken.append(line)
                    if funcToken.balanceBracket(line):
                        self.addMethodSource(funcToken)
                        funcToken = None



    def addMethodSource(self, funcToken):
        source = funcToken.body
        print("func:", funcToken.start.lineno, '-', funcToken.stop.lineno)
        func = FuncHash(dict(path=self.path,
                                start=funcToken.start.lineno,
                                startLoc={
                                    "line": funcToken.start.lineno,
                                    "column": 0
                                },
                                stop=funcToken.stop.lineno,
                                stopLoc={
                                    "line": funcToken.stop.lineno,
                                    "column": 0
                                },
                                source=source,
                                blame=self.blamer.getBlame(funcToken.start.lineno)))

        self.funcList.append(func)

        pass

    def hasCopyTag(self, source):
        for line in source.split('\n'):
            line = line.strip()
            if line.startswith("//"):
                if re.match(r"//.*COPY", line):
                    return True
        return False
