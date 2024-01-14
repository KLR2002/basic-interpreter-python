# Generated from ./BasicExpression.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .BasicExpressionParser import BasicExpressionParser
else:
    from BasicExpressionParser import BasicExpressionParser

# This class defines a complete listener for a parse tree produced by BasicExpressionParser.
class BasicExpressionListener(ParseTreeListener):

    # Enter a parse tree produced by BasicExpressionParser#prog.
    def enterProg(self, ctx:BasicExpressionParser.ProgContext):
        pass

    # Exit a parse tree produced by BasicExpressionParser#prog.
    def exitProg(self, ctx:BasicExpressionParser.ProgContext):
        pass


    # Enter a parse tree produced by BasicExpressionParser#stat.
    def enterStat(self, ctx:BasicExpressionParser.StatContext):
        pass

    # Exit a parse tree produced by BasicExpressionParser#stat.
    def exitStat(self, ctx:BasicExpressionParser.StatContext):
        pass


    # Enter a parse tree produced by BasicExpressionParser#AndExpr.
    def enterAndExpr(self, ctx:BasicExpressionParser.AndExprContext):
        pass

    # Exit a parse tree produced by BasicExpressionParser#AndExpr.
    def exitAndExpr(self, ctx:BasicExpressionParser.AndExprContext):
        pass


    # Enter a parse tree produced by BasicExpressionParser#StringExpr.
    def enterStringExpr(self, ctx:BasicExpressionParser.StringExprContext):
        pass

    # Exit a parse tree produced by BasicExpressionParser#StringExpr.
    def exitStringExpr(self, ctx:BasicExpressionParser.StringExprContext):
        pass


    # Enter a parse tree produced by BasicExpressionParser#FloatExpr.
    def enterFloatExpr(self, ctx:BasicExpressionParser.FloatExprContext):
        pass

    # Exit a parse tree produced by BasicExpressionParser#FloatExpr.
    def exitFloatExpr(self, ctx:BasicExpressionParser.FloatExprContext):
        pass


    # Enter a parse tree produced by BasicExpressionParser#IdExpr.
    def enterIdExpr(self, ctx:BasicExpressionParser.IdExprContext):
        pass

    # Exit a parse tree produced by BasicExpressionParser#IdExpr.
    def exitIdExpr(self, ctx:BasicExpressionParser.IdExprContext):
        pass


    # Enter a parse tree produced by BasicExpressionParser#RelExpr.
    def enterRelExpr(self, ctx:BasicExpressionParser.RelExprContext):
        pass

    # Exit a parse tree produced by BasicExpressionParser#RelExpr.
    def exitRelExpr(self, ctx:BasicExpressionParser.RelExprContext):
        pass


    # Enter a parse tree produced by BasicExpressionParser#ExpExpr.
    def enterExpExpr(self, ctx:BasicExpressionParser.ExpExprContext):
        pass

    # Exit a parse tree produced by BasicExpressionParser#ExpExpr.
    def exitExpExpr(self, ctx:BasicExpressionParser.ExpExprContext):
        pass


    # Enter a parse tree produced by BasicExpressionParser#FuncExpr.
    def enterFuncExpr(self, ctx:BasicExpressionParser.FuncExprContext):
        pass

    # Exit a parse tree produced by BasicExpressionParser#FuncExpr.
    def exitFuncExpr(self, ctx:BasicExpressionParser.FuncExprContext):
        pass


    # Enter a parse tree produced by BasicExpressionParser#OrExpr.
    def enterOrExpr(self, ctx:BasicExpressionParser.OrExprContext):
        pass

    # Exit a parse tree produced by BasicExpressionParser#OrExpr.
    def exitOrExpr(self, ctx:BasicExpressionParser.OrExprContext):
        pass


    # Enter a parse tree produced by BasicExpressionParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:BasicExpressionParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by BasicExpressionParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:BasicExpressionParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by BasicExpressionParser#ArrExpr.
    def enterArrExpr(self, ctx:BasicExpressionParser.ArrExprContext):
        pass

    # Exit a parse tree produced by BasicExpressionParser#ArrExpr.
    def exitArrExpr(self, ctx:BasicExpressionParser.ArrExprContext):
        pass


    # Enter a parse tree produced by BasicExpressionParser#unaryMinusExpr.
    def enterUnaryMinusExpr(self, ctx:BasicExpressionParser.UnaryMinusExprContext):
        pass

    # Exit a parse tree produced by BasicExpressionParser#unaryMinusExpr.
    def exitUnaryMinusExpr(self, ctx:BasicExpressionParser.UnaryMinusExprContext):
        pass


    # Enter a parse tree produced by BasicExpressionParser#NumberExpr.
    def enterNumberExpr(self, ctx:BasicExpressionParser.NumberExprContext):
        pass

    # Exit a parse tree produced by BasicExpressionParser#NumberExpr.
    def exitNumberExpr(self, ctx:BasicExpressionParser.NumberExprContext):
        pass


    # Enter a parse tree produced by BasicExpressionParser#NotExpr.
    def enterNotExpr(self, ctx:BasicExpressionParser.NotExprContext):
        pass

    # Exit a parse tree produced by BasicExpressionParser#NotExpr.
    def exitNotExpr(self, ctx:BasicExpressionParser.NotExprContext):
        pass


    # Enter a parse tree produced by BasicExpressionParser#ParenExpr.
    def enterParenExpr(self, ctx:BasicExpressionParser.ParenExprContext):
        pass

    # Exit a parse tree produced by BasicExpressionParser#ParenExpr.
    def exitParenExpr(self, ctx:BasicExpressionParser.ParenExprContext):
        pass


    # Enter a parse tree produced by BasicExpressionParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:BasicExpressionParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by BasicExpressionParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:BasicExpressionParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by BasicExpressionParser#func.
    def enterFunc(self, ctx:BasicExpressionParser.FuncContext):
        pass

    # Exit a parse tree produced by BasicExpressionParser#func.
    def exitFunc(self, ctx:BasicExpressionParser.FuncContext):
        pass


    # Enter a parse tree produced by BasicExpressionParser#string.
    def enterString(self, ctx:BasicExpressionParser.StringContext):
        pass

    # Exit a parse tree produced by BasicExpressionParser#string.
    def exitString(self, ctx:BasicExpressionParser.StringContext):
        pass


    # Enter a parse tree produced by BasicExpressionParser#number.
    def enterNumber(self, ctx:BasicExpressionParser.NumberContext):
        pass

    # Exit a parse tree produced by BasicExpressionParser#number.
    def exitNumber(self, ctx:BasicExpressionParser.NumberContext):
        pass


    # Enter a parse tree produced by BasicExpressionParser#float.
    def enterFloat(self, ctx:BasicExpressionParser.FloatContext):
        pass

    # Exit a parse tree produced by BasicExpressionParser#float.
    def exitFloat(self, ctx:BasicExpressionParser.FloatContext):
        pass


    # Enter a parse tree produced by BasicExpressionParser#id.
    def enterId(self, ctx:BasicExpressionParser.IdContext):
        pass

    # Exit a parse tree produced by BasicExpressionParser#id.
    def exitId(self, ctx:BasicExpressionParser.IdContext):
        pass


    # Enter a parse tree produced by BasicExpressionParser#lenfunc.
    def enterLenfunc(self, ctx:BasicExpressionParser.LenfuncContext):
        pass

    # Exit a parse tree produced by BasicExpressionParser#lenfunc.
    def exitLenfunc(self, ctx:BasicExpressionParser.LenfuncContext):
        pass


    # Enter a parse tree produced by BasicExpressionParser#valfunc.
    def enterValfunc(self, ctx:BasicExpressionParser.ValfuncContext):
        pass

    # Exit a parse tree produced by BasicExpressionParser#valfunc.
    def exitValfunc(self, ctx:BasicExpressionParser.ValfuncContext):
        pass


    # Enter a parse tree produced by BasicExpressionParser#isnanfunc.
    def enterIsnanfunc(self, ctx:BasicExpressionParser.IsnanfuncContext):
        pass

    # Exit a parse tree produced by BasicExpressionParser#isnanfunc.
    def exitIsnanfunc(self, ctx:BasicExpressionParser.IsnanfuncContext):
        pass


    # Enter a parse tree produced by BasicExpressionParser#randfunc.
    def enterRandfunc(self, ctx:BasicExpressionParser.RandfuncContext):
        pass

    # Exit a parse tree produced by BasicExpressionParser#randfunc.
    def exitRandfunc(self, ctx:BasicExpressionParser.RandfuncContext):
        pass



del BasicExpressionParser