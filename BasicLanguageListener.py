# Generated from ./BasicLanguage.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .BasicLanguageParser import BasicLanguageParser
else:
    from BasicLanguageParser import BasicLanguageParser

# This class defines a complete listener for a parse tree produced by BasicLanguageParser.
class BasicLanguageListener(ParseTreeListener):

    # Enter a parse tree produced by BasicLanguageParser#prog.
    def enterProg(self, ctx:BasicLanguageParser.ProgContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#prog.
    def exitProg(self, ctx:BasicLanguageParser.ProgContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#statement.
    def enterStatement(self, ctx:BasicLanguageParser.StatementContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#statement.
    def exitStatement(self, ctx:BasicLanguageParser.StatementContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#block.
    def enterBlock(self, ctx:BasicLanguageParser.BlockContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#block.
    def exitBlock(self, ctx:BasicLanguageParser.BlockContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#letStmt.
    def enterLetStmt(self, ctx:BasicLanguageParser.LetStmtContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#letStmt.
    def exitLetStmt(self, ctx:BasicLanguageParser.LetStmtContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#arrStmt.
    def enterArrStmt(self, ctx:BasicLanguageParser.ArrStmtContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#arrStmt.
    def exitArrStmt(self, ctx:BasicLanguageParser.ArrStmtContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#arrElementStmt.
    def enterArrElementStmt(self, ctx:BasicLanguageParser.ArrElementStmtContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#arrElementStmt.
    def exitArrElementStmt(self, ctx:BasicLanguageParser.ArrElementStmtContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#vardecl.
    def enterVardecl(self, ctx:BasicLanguageParser.VardeclContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#vardecl.
    def exitVardecl(self, ctx:BasicLanguageParser.VardeclContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#varname.
    def enterVarname(self, ctx:BasicLanguageParser.VarnameContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#varname.
    def exitVarname(self, ctx:BasicLanguageParser.VarnameContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#varsuffix.
    def enterVarsuffix(self, ctx:BasicLanguageParser.VarsuffixContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#varsuffix.
    def exitVarsuffix(self, ctx:BasicLanguageParser.VarsuffixContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#printStmt.
    def enterPrintStmt(self, ctx:BasicLanguageParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#printStmt.
    def exitPrintStmt(self, ctx:BasicLanguageParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#inputStmt.
    def enterInputStmt(self, ctx:BasicLanguageParser.InputStmtContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#inputStmt.
    def exitInputStmt(self, ctx:BasicLanguageParser.InputStmtContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#ifStmt.
    def enterIfStmt(self, ctx:BasicLanguageParser.IfStmtContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#ifStmt.
    def exitIfStmt(self, ctx:BasicLanguageParser.IfStmtContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#elifStmt.
    def enterElifStmt(self, ctx:BasicLanguageParser.ElifStmtContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#elifStmt.
    def exitElifStmt(self, ctx:BasicLanguageParser.ElifStmtContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#elseStmt.
    def enterElseStmt(self, ctx:BasicLanguageParser.ElseStmtContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#elseStmt.
    def exitElseStmt(self, ctx:BasicLanguageParser.ElseStmtContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#subStmt.
    def enterSubStmt(self, ctx:BasicLanguageParser.SubStmtContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#subStmt.
    def exitSubStmt(self, ctx:BasicLanguageParser.SubStmtContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#subCall.
    def enterSubCall(self, ctx:BasicLanguageParser.SubCallContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#subCall.
    def exitSubCall(self, ctx:BasicLanguageParser.SubCallContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#forStmt.
    def enterForStmt(self, ctx:BasicLanguageParser.ForStmtContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#forStmt.
    def exitForStmt(self, ctx:BasicLanguageParser.ForStmtContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#whileStmt.
    def enterWhileStmt(self, ctx:BasicLanguageParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#whileStmt.
    def exitWhileStmt(self, ctx:BasicLanguageParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#repeatStmt.
    def enterRepeatStmt(self, ctx:BasicLanguageParser.RepeatStmtContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#repeatStmt.
    def exitRepeatStmt(self, ctx:BasicLanguageParser.RepeatStmtContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#continueStmt.
    def enterContinueStmt(self, ctx:BasicLanguageParser.ContinueStmtContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#continueStmt.
    def exitContinueStmt(self, ctx:BasicLanguageParser.ContinueStmtContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#exitStmt.
    def enterExitStmt(self, ctx:BasicLanguageParser.ExitStmtContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#exitStmt.
    def exitExitStmt(self, ctx:BasicLanguageParser.ExitStmtContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#swapFunc.
    def enterSwapFunc(self, ctx:BasicLanguageParser.SwapFuncContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#swapFunc.
    def exitSwapFunc(self, ctx:BasicLanguageParser.SwapFuncContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#stat.
    def enterStat(self, ctx:BasicLanguageParser.StatContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#stat.
    def exitStat(self, ctx:BasicLanguageParser.StatContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#AndExpr.
    def enterAndExpr(self, ctx:BasicLanguageParser.AndExprContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#AndExpr.
    def exitAndExpr(self, ctx:BasicLanguageParser.AndExprContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#StringExpr.
    def enterStringExpr(self, ctx:BasicLanguageParser.StringExprContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#StringExpr.
    def exitStringExpr(self, ctx:BasicLanguageParser.StringExprContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#FloatExpr.
    def enterFloatExpr(self, ctx:BasicLanguageParser.FloatExprContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#FloatExpr.
    def exitFloatExpr(self, ctx:BasicLanguageParser.FloatExprContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#IdExpr.
    def enterIdExpr(self, ctx:BasicLanguageParser.IdExprContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#IdExpr.
    def exitIdExpr(self, ctx:BasicLanguageParser.IdExprContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#RelExpr.
    def enterRelExpr(self, ctx:BasicLanguageParser.RelExprContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#RelExpr.
    def exitRelExpr(self, ctx:BasicLanguageParser.RelExprContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#ExpExpr.
    def enterExpExpr(self, ctx:BasicLanguageParser.ExpExprContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#ExpExpr.
    def exitExpExpr(self, ctx:BasicLanguageParser.ExpExprContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#FuncExpr.
    def enterFuncExpr(self, ctx:BasicLanguageParser.FuncExprContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#FuncExpr.
    def exitFuncExpr(self, ctx:BasicLanguageParser.FuncExprContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#OrExpr.
    def enterOrExpr(self, ctx:BasicLanguageParser.OrExprContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#OrExpr.
    def exitOrExpr(self, ctx:BasicLanguageParser.OrExprContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#MulDivExpr.
    def enterMulDivExpr(self, ctx:BasicLanguageParser.MulDivExprContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#MulDivExpr.
    def exitMulDivExpr(self, ctx:BasicLanguageParser.MulDivExprContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#ArrExpr.
    def enterArrExpr(self, ctx:BasicLanguageParser.ArrExprContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#ArrExpr.
    def exitArrExpr(self, ctx:BasicLanguageParser.ArrExprContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#unaryMinusExpr.
    def enterUnaryMinusExpr(self, ctx:BasicLanguageParser.UnaryMinusExprContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#unaryMinusExpr.
    def exitUnaryMinusExpr(self, ctx:BasicLanguageParser.UnaryMinusExprContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#NumberExpr.
    def enterNumberExpr(self, ctx:BasicLanguageParser.NumberExprContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#NumberExpr.
    def exitNumberExpr(self, ctx:BasicLanguageParser.NumberExprContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#NotExpr.
    def enterNotExpr(self, ctx:BasicLanguageParser.NotExprContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#NotExpr.
    def exitNotExpr(self, ctx:BasicLanguageParser.NotExprContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#ParenExpr.
    def enterParenExpr(self, ctx:BasicLanguageParser.ParenExprContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#ParenExpr.
    def exitParenExpr(self, ctx:BasicLanguageParser.ParenExprContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#AddSubExpr.
    def enterAddSubExpr(self, ctx:BasicLanguageParser.AddSubExprContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#AddSubExpr.
    def exitAddSubExpr(self, ctx:BasicLanguageParser.AddSubExprContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#func.
    def enterFunc(self, ctx:BasicLanguageParser.FuncContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#func.
    def exitFunc(self, ctx:BasicLanguageParser.FuncContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#string.
    def enterString(self, ctx:BasicLanguageParser.StringContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#string.
    def exitString(self, ctx:BasicLanguageParser.StringContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#number.
    def enterNumber(self, ctx:BasicLanguageParser.NumberContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#number.
    def exitNumber(self, ctx:BasicLanguageParser.NumberContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#float.
    def enterFloat(self, ctx:BasicLanguageParser.FloatContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#float.
    def exitFloat(self, ctx:BasicLanguageParser.FloatContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#id.
    def enterId(self, ctx:BasicLanguageParser.IdContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#id.
    def exitId(self, ctx:BasicLanguageParser.IdContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#lenfunc.
    def enterLenfunc(self, ctx:BasicLanguageParser.LenfuncContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#lenfunc.
    def exitLenfunc(self, ctx:BasicLanguageParser.LenfuncContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#valfunc.
    def enterValfunc(self, ctx:BasicLanguageParser.ValfuncContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#valfunc.
    def exitValfunc(self, ctx:BasicLanguageParser.ValfuncContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#isnanfunc.
    def enterIsnanfunc(self, ctx:BasicLanguageParser.IsnanfuncContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#isnanfunc.
    def exitIsnanfunc(self, ctx:BasicLanguageParser.IsnanfuncContext):
        pass


    # Enter a parse tree produced by BasicLanguageParser#randfunc.
    def enterRandfunc(self, ctx:BasicLanguageParser.RandfuncContext):
        pass

    # Exit a parse tree produced by BasicLanguageParser#randfunc.
    def exitRandfunc(self, ctx:BasicLanguageParser.RandfuncContext):
        pass



del BasicLanguageParser