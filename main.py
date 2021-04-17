# coding: utf-8

import sys
from antlr4 import *
from grammar import *

class OCCodeListener(ObjectiveCParserListener):

    def __init__(self, inputStream):
        super()
        self.inputStream = inputStream

    def enterInstanceMethodDefinition(self, ctx):
        print("impl", ctx.getToken(ctx.start, ctx.stop))
        print(self.inputStream.getText(ctx.start.start, ctx.stop.stop))
        pass

    def enterCategoryImplementation(self, ctx):
        pass


def main(argv):
    input_stream = FileStream(argv[1], "utf8")
    lexer = ObjectiveCLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ObjectiveCParser(stream)

    tree = parser.translationUnit()

    listener = OCCodeListener(input_stream)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
 
if __name__ == '__main__':
    main(sys.argv)