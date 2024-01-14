# Generated from ./BasicLanguage.g4 by ANTLR 4.13.1
import random

from antlr4 import *
from BasicValue import Value
from BasicExpressionParser import BasicExpressionParser
from CustomException import *
if "." in __name__:
    from .BasicLanguageParser import BasicLanguageParser
else:
    from BasicLanguageParser import BasicLanguageParser

# This class defines a complete generic visitor for a parse tree produced by BasicLanguageParser.

class BasicLanguageVisitor(ParseTreeVisitor):
    def __init__(self):
        self.memory = {}
        self.functions = {}

    # Visit a parse tree produced by BasicLanguageParser#prog.
    def visitProg(self, ctx:BasicLanguageParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicLanguageParser#statement.
    def visitStatement(self, ctx:BasicLanguageParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicLanguageParser#block.
    def visitBlock(self, ctx:BasicLanguageParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicLanguageParser#letStmt.
    def visitLetStmt(self, ctx:BasicLanguageParser.LetStmtContext):
        varname = ctx.vardecl().varname().ID().getText()
        value = self.visit(ctx.expression())
        self.memory[varname] = value
        return value

    def visitArrStmt(self, ctx:BasicLanguageParser.ArrStmtContext):
        varname = ctx.vardecl().varname().ID().getText()
        size = self.visit(ctx.expression())
        value = Value([Value(0) for _ in range(size.internal_number())])
        self.memory[varname] = value
        return value

    def visitArrElementStmt(self, ctx:BasicLanguageParser.ArrElementStmtContext):
        arr_name = ctx.varname().ID().getText()
        index = self.visit(ctx.expression(0))
        value = self.visit(ctx.expression(1))
        val = Value(value.internal_number())
        arr = self.memory[arr_name].internal_array()
        arr[index.internal_number()] = val
        self.memory[arr_name] = Value(arr)
        return val

    # Visit a parse tree produced by BasicLanguageParser#vardecl.
    def visitVardecl(self, ctx:BasicLanguageParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicLanguageParser#varname.
    def visitVarname(self, ctx:BasicLanguageParser.VarnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicLanguageParser#varsuffix.
    def visitVarsuffix(self, ctx:BasicLanguageParser.VarsuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicLanguageParser#printStmt.
    def visitPrintStmt(self, ctx:BasicLanguageParser.PrintStmtContext):
        val = self.visit(ctx.expression())
        if val.is_number() or val.is_string():
            print(val.value)
        else:
            print("[",end="")
            for i, element in enumerate(val.internal_array()):
                print(element.value, end="")
                if i == len(val.internal_array())-1:
                    print("]")
                else:
                    print(",", end=" ")

        return val


    # Visit a parse tree produced by BasicLanguageParser#inputStmt.
    def visitInputStmt(self, ctx:BasicLanguageParser.InputStmtContext):
        message = self.visit(ctx.string()).internal_string() + ' '
        varname = ctx.vardecl().getText()
        inpt = input(message)
        val = Value(inpt)
        self.memory[varname] = val
        return val


    # Visit a parse tree produced by BasicLanguageParser#ifStmt.
    def visitIfStmt(self, ctx:BasicLanguageParser.IfStmtContext):
        condition = self.visit(ctx.expression())
        if condition.is_true():
            return self.visit(ctx.block())
        else:
            for elif_ctx in ctx.elifStmt():
                condition = self.visit(elif_ctx.expression())
                if condition.is_true():
                    return self.visit(elif_ctx.block())

            if ctx.elseStmt() is not None:
                return self.visit(ctx.elseStmt().block())

        return condition


    # Visit a parse tree produced by BasicLanguageParser#elifStmt.
    def visitElifStmt(self, ctx:BasicLanguageParser.ElifStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicLanguageParser#elseStmt.
    def visitElseStmt(self, ctx:BasicLanguageParser.ElseStmtContext):
        return self.visitChildren(ctx)

    def visitSubStmt(self, ctx:BasicLanguageParser.SubStmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BasicLanguageParser#subCall.
    def visitSubCall(self, ctx:BasicLanguageParser.SubCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicLanguageParser#forStmt.
    def visitForStmt(self, ctx:BasicLanguageParser.ForStmtContext):
        varname = ctx.vardecl().varname().ID().getText()
        start = self.visit(ctx.expression(0))
        end = self.visit(ctx.expression(1))
        if ctx.expression(2) is not None:
            step = self.visit(ctx.expression(2))
        else:
            step = Value(1)

        for i in range(start.internal_number(), end.internal_number() + 1, step.internal_number()):
            self.memory[varname] = Value(i)
            try:
                self.visit(ctx.block())
            except ContinueException:
                continue
            except BreakException:
                break

        return Value(0)


    # Visit a parse tree produced by BasicLanguageParser#whileStmt.
    def visitWhileStmt(self, ctx:BasicLanguageParser.WhileStmtContext):
        condition = self.visit(ctx.expression())
        while condition.is_true():
            try:
                self.visit(ctx.block())
            except ContinueException:
                continue
            except BreakException:
                break
            finally:
                condition = self.visit(ctx.expression())

        return Value(0)


    # Visit a parse tree produced by BasicLanguageParser#repeatStmt.
    def visitRepeatStmt(self, ctx:BasicLanguageParser.RepeatStmtContext):
        condition = Value(0)
        while condition.is_false():
            try:
                self.visit(ctx.block())
            except ContinueException:
                continue
            except BreakException:
                break
            finally:
                condition = self.visit(ctx.expression())
        return Value(0)

    # Visit a parse tree produced by BasicLanguageParser#continueStmt.
    def visitContinueStmt(self, ctx:BasicLanguageParser.ContinueStmtContext):
        raise ContinueException


    # Visit a parse tree produced by BasicLanguageParser#exitStmt.
    def visitExitStmt(self, ctx:BasicLanguageParser.ExitStmtContext):
        raise BreakException

    def visitSwapFunc(self, ctx:BasicLanguageParser.SwapFuncContext):
        x = self.visit(ctx.expression(0))
        y = self.visit(ctx.expression(1))
        z = Value(x.value)
        x.change_value(y.value)
        y.change_value(z.value)
        return x,y


    # Visit a parse tree produced by BasicLanguageParser#stat.
    def visitStat(self, ctx:BasicLanguageParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicLanguageParser#AndExpr.
    def visitAndExpr(self, ctx:BasicLanguageParser.AndExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left.mand(right)


    # Visit a parse tree produced by BasicLanguageParser#StringExpr.
    def visitStringExpr(self, ctx:BasicLanguageParser.StringExprContext):
        return self.visitChildren(ctx)

    def visitFloatExpr(self, ctx:BasicLanguageParser.FloatExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by BasicLanguageParser#MulDivExpr.
    def visitMulDivExpr(self, ctx:BasicLanguageParser.MulDivExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        if ctx.op.type == BasicExpressionParser.MUL:
            return left.mul(right)
        elif ctx.op.type == BasicExpressionParser.DIV:
            return left.idiv(right)
        elif ctx.op.type == BasicExpressionParser.IDIV:
            return left.idiv(right)
        else:
            if left.is_float() or right.is_float():
                raise ValueError
            return left.mod(right)

    def visitArrExpr(self, ctx:BasicLanguageParser.ArrExprContext):
        arr_name = ctx.expression(0).getText()
        index = self.visit(ctx.expression(1))

        if(self.memory.get(arr_name).is_array()):
            return self.memory.get(arr_name).internal_array()[index.internal_number()]
        else:
            return Value(self.memory.get(arr_name).internal_string()[index.internal_number()])
        #return self.visitChildren(ctx)

    def visitUnaryMinusExpr(self, ctx:BasicLanguageParser.UnaryMinusExprContext):
        val = self.visit(ctx.expression())
        minus = Value(-1)
        return val.mul(minus)

    # Visit a parse tree produced by BasicLanguageParser#IdExpr.
    def visitIdExpr(self, ctx:BasicLanguageParser.IdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicLanguageParser#NumberExpr.
    def visitNumberExpr(self, ctx:BasicLanguageParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicLanguageParser#RelExpr.
    def visitRelExpr(self, ctx:BasicLanguageParser.RelExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))

        match ctx.op.type:
            case BasicExpressionParser.GT:
                return left.gt(right)
            case BasicExpressionParser.GTE:
                return left.gte(right)
            case BasicExpressionParser.LT:
                return left.lt(right)
            case BasicExpressionParser.LTE:
                return left.lte(right)
            case BasicExpressionParser.EQ:
                return left.eq(right)
            case _:
                return left.neq(right)


    # Visit a parse tree produced by BasicLanguageParser#NotExpr.
    def visitNotExpr(self, ctx:BasicLanguageParser.NotExprContext):
        val = self.visit(ctx.expression())
        return val.mnot()


    # Visit a parse tree produced by BasicLanguageParser#ParenExpr.
    def visitParenExpr(self, ctx:BasicLanguageParser.ParenExprContext):
        return self.visit(ctx.expression())
        #return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicLanguageParser#ExpExpr.
    def visitExpExpr(self, ctx:BasicLanguageParser.ExpExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left.exp(right)


    # Visit a parse tree produced by BasicLanguageParser#FuncExpr.
    def visitFuncExpr(self, ctx:BasicLanguageParser.FuncExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicLanguageParser#AddSubExpr.
    def visitAddSubExpr(self, ctx:BasicLanguageParser.AddSubExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        if ctx.op.type == BasicExpressionParser.ADD:
            return left.add(right)
        else:
            return left.sub(right)


    # Visit a parse tree produced by BasicLanguageParser#OrExpr.
    def visitOrExpr(self, ctx:BasicLanguageParser.OrExprContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        return left.mor(right)


    # Visit a parse tree produced by BasicLanguageParser#func.
    def visitFunc(self, ctx:BasicLanguageParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BasicLanguageParser#string.
    def visitString(self, ctx:BasicLanguageParser.StringContext):
        s = ctx.getText()
        return Value(s[1:len(s) - 1])


    # Visit a parse tree produced by BasicLanguageParser#number.
    def visitNumber(self, ctx:BasicLanguageParser.NumberContext):
        return Value(int(ctx.getText()))

        # Visit a parse tree produced by BasicLanguageParser#float.
    def visitFloat(self, ctx: BasicLanguageParser.FloatContext):
        return Value(float(ctx.getText()))

    # Visit a parse tree produced by BasicLanguageParser#id.
    def visitId(self, ctx:BasicLanguageParser.IdContext):
        return self.memory.get(ctx.getText())


    # Visit a parse tree produced by BasicLanguageParser#lenfunc.
    def visitLenfunc(self, ctx:BasicLanguageParser.LenfuncContext):
        s = self.visit(ctx.expression())
        try:
            if s.is_string():
                return Value(len(s.internal_string()))
            elif s.is_array():
                return Value(len(s.internal_array()))
            else:
                raise ValueError("Argument is not string or array")
        except ValueError:
            raise


    # Visit a parse tree produced by BasicLanguageParser#valfunc.
    def visitValfunc(self, ctx:BasicLanguageParser.ValfuncContext):
        val = self.visit(ctx.expression())
        if val.is_string():
            s = val.internal_string()
            try:
                if '.' in s:
                    return Value(float(s))
                else:
                    return Value(int(s))
            except ValueError:
                return Value(None, True)
        else:
            return val


    # Visit a parse tree produced by BasicLanguageParser#isnanfunc.
    def visitIsnanfunc(self, ctx:BasicLanguageParser.IsnanfuncContext):
        n = self.visit(ctx.expression())
        if n.check_none():
            return Value(1)
        else:
            return Value(0)

    def visitRandfunc(self, ctx:BasicLanguageParser.RandfuncContext):
        a = self.visit(ctx.expression(0))
        b = self.visit(ctx.expression(1))

        return Value(random.randint(a.internal_number(), b.internal_number()))


del BasicLanguageParser