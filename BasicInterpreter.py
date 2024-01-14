from antlr4 import *

from BasicLanguageLexer import BasicLanguageLexer
from BasicLanguageParser import BasicLanguageParser
from BasicLanguageVisitor import BasicLanguageVisitor


class Interpreter:
    def interpret(self, input_name):
        input_file = FileStream(input_name)
        lexer = BasicLanguageLexer(input_file)
        tokens = CommonTokenStream(lexer)
        parser = BasicLanguageParser(tokens)

        tree = parser.prog()
        evaluate = BasicLanguageVisitor()
        evaluate.visit(tree)
