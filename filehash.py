# coding: utf-8


import sys
import os
from antlr4 import *
from grammar import *
from funchash import FuncHash

class OCCodeListener(ObjectiveCParserListener):

    def __init__(self, fileHash):
        super()
        self.fileHash = fileHash

    def enterInstanceMethodDefinition(self, ctx):
        self.addList(ctx)

    def enterCategoryImplementation(self, ctx):
        self.addList(ctx)


    def addList(self, ctx):
        self.fileHash.addMethodSource(ctx.start.start, ctx.stop.stop)
        pass

class FileHash:

    def __init__(self, path):
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


    def addMethodSource(self, start, stop):
        source = self.fileStream.getText(start, stop)

        func = FuncHash(dict(path=self.path,
                                start=start,
                                stop=stop,
                                source=source))

        self.funcList.append(func)

        pass