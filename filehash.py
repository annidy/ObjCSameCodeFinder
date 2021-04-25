# coding: utf-8


import sys
import os
from antlr4 import *
from grammar import *
from FuncHash import FuncHash
from Blamer import Blamer

class OCCodeListener(ObjectiveCParserListener):

    def __init__(self, fileHash):
        super()
        self.fileHash = fileHash

    def enterInstanceMethodDefinition(self, ctx):
        self.addList(ctx)

    def enterClassMethodDeclaration(self, ctx):
        self.addList(ctx)


    def addList(self, ctx):
        self.fileHash.addMethodSource(ctx.start, ctx.stop)
        pass

class FileHash:

    def __init__(self, path):
        self.blamer = Blamer(path)
        self.funcList = []
        self.path = path
        self.fileStream = FileStream(path, "utf8")

        lexer = ObjectiveCLexer(self.fileStream)
        stream = CommonTokenStream(lexer)
        parser = ObjectiveCParser(stream)

        tree = parser.translationUnit()

        listener = OCCodeListener(self)
        walker = ParseTreeWalker()
        walker.walk(listener, tree)


    def addMethodSource(self, start: Token, stop: Token):
        source = self.fileStream.getText(start.start, stop.stop)

        func = FuncHash(dict(path=self.path,
                                start=start.start,
                                startLoc={
                                    "line": start.line,
                                    "column": start.column
                                },
                                stop=stop.stop,
                                stopLoc={
                                    "line": stop.line,
                                    "column": stop.column
                                },
                                source=source,
                                blame=self.blamer.getBlame(start.line)))

        self.funcList.append(func)

        pass