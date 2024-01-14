# Generated from ./BasicExpression.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,54,116,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,4,0,26,8,0,11,
        0,12,0,27,1,1,1,1,1,1,1,1,3,1,34,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,50,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,5,2,75,8,2,10,2,12,2,78,9,2,1,3,1,3,1,3,1,3,3,3,84,8,3,1,4,1,4,
        1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,
        1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,
        0,1,4,12,0,2,4,6,8,10,12,14,16,18,20,22,0,3,2,0,1,3,7,7,1,0,4,5,
        1,0,8,13,122,0,25,1,0,0,0,2,33,1,0,0,0,4,49,1,0,0,0,6,83,1,0,0,0,
        8,85,1,0,0,0,10,87,1,0,0,0,12,89,1,0,0,0,14,91,1,0,0,0,16,93,1,0,
        0,0,18,98,1,0,0,0,20,103,1,0,0,0,22,108,1,0,0,0,24,26,3,2,1,0,25,
        24,1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,1,1,0,0,
        0,29,30,3,4,2,0,30,31,5,53,0,0,31,34,1,0,0,0,32,34,5,53,0,0,33,29,
        1,0,0,0,33,32,1,0,0,0,34,3,1,0,0,0,35,36,6,2,-1,0,36,37,5,5,0,0,
        37,50,3,4,2,15,38,50,3,8,4,0,39,50,3,10,5,0,40,50,3,12,6,0,41,50,
        3,6,3,0,42,50,3,14,7,0,43,44,5,18,0,0,44,45,3,4,2,0,45,46,5,19,0,
        0,46,50,1,0,0,0,47,48,5,16,0,0,48,50,3,4,2,4,49,35,1,0,0,0,49,38,
        1,0,0,0,49,39,1,0,0,0,49,40,1,0,0,0,49,41,1,0,0,0,49,42,1,0,0,0,
        49,43,1,0,0,0,49,47,1,0,0,0,50,76,1,0,0,0,51,52,10,7,0,0,52,53,7,
        0,0,0,53,75,3,4,2,8,54,55,10,6,0,0,55,56,7,1,0,0,56,75,3,4,2,7,57,
        58,10,5,0,0,58,59,7,2,0,0,59,75,3,4,2,6,60,61,10,3,0,0,61,62,5,14,
        0,0,62,75,3,4,2,4,63,64,10,2,0,0,64,65,5,15,0,0,65,75,3,4,2,3,66,
        67,10,1,0,0,67,68,5,6,0,0,68,75,3,4,2,1,69,70,10,8,0,0,70,71,5,20,
        0,0,71,72,3,4,2,0,72,73,5,21,0,0,73,75,1,0,0,0,74,51,1,0,0,0,74,
        54,1,0,0,0,74,57,1,0,0,0,74,60,1,0,0,0,74,63,1,0,0,0,74,66,1,0,0,
        0,74,69,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,5,1,
        0,0,0,78,76,1,0,0,0,79,84,3,16,8,0,80,84,3,18,9,0,81,84,3,20,10,
        0,82,84,3,22,11,0,83,79,1,0,0,0,83,80,1,0,0,0,83,81,1,0,0,0,83,82,
        1,0,0,0,84,7,1,0,0,0,85,86,5,51,0,0,86,9,1,0,0,0,87,88,5,49,0,0,
        88,11,1,0,0,0,89,90,5,50,0,0,90,13,1,0,0,0,91,92,5,48,0,0,92,15,
        1,0,0,0,93,94,5,22,0,0,94,95,5,18,0,0,95,96,3,4,2,0,96,97,5,19,0,
        0,97,17,1,0,0,0,98,99,5,23,0,0,99,100,5,18,0,0,100,101,3,4,2,0,101,
        102,5,19,0,0,102,19,1,0,0,0,103,104,5,24,0,0,104,105,5,18,0,0,105,
        106,3,4,2,0,106,107,5,19,0,0,107,21,1,0,0,0,108,109,5,25,0,0,109,
        110,5,18,0,0,110,111,3,4,2,0,111,112,5,17,0,0,112,113,3,4,2,0,113,
        114,5,19,0,0,114,23,1,0,0,0,6,27,33,49,74,76,83
    ]

class BasicExpressionParser ( Parser ):

    grammarFileName = "BasicExpression.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'/'", "'DIV'", "'+'", "'-'", "'^'", 
                     "'MOD'", "'<>'", "'>='", "'<='", "'>'", "'<'", "'='", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "','", "'('", 
                     "')'", "'['", "']'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'$'" ]

    symbolicNames = [ "<INVALID>", "MUL", "DIV", "IDIV", "ADD", "SUB", "EXP", 
                      "MOD", "NEQ", "GTE", "LTE", "GT", "LT", "EQ", "AND", 
                      "OR", "NOT", "COMMA", "LPAREN", "RPAREN", "LPARENSQ", 
                      "RPARENSQ", "LEN", "VAL", "ISNAN", "RAND", "SWAP", 
                      "PRINT", "INPUT", "LET", "DIM", "INDEX", "REM", "IF", 
                      "THEN", "ELSE", "END", "SUBROUTINE", "FOR", "WHILE", 
                      "REPEAT", "UNTIL", "STEP", "NEXT", "TO", "CONTINUE", 
                      "EXIT", "COMMENT", "ID", "NUMBER", "FLOAT", "STRINGLITERAL", 
                      "DOLLAR", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expression = 2
    RULE_func = 3
    RULE_string = 4
    RULE_number = 5
    RULE_float = 6
    RULE_id = 7
    RULE_lenfunc = 8
    RULE_valfunc = 9
    RULE_isnanfunc = 10
    RULE_randfunc = 11

    ruleNames =  [ "prog", "stat", "expression", "func", "string", "number", 
                   "float", "id", "lenfunc", "valfunc", "isnanfunc", "randfunc" ]

    EOF = Token.EOF
    MUL=1
    DIV=2
    IDIV=3
    ADD=4
    SUB=5
    EXP=6
    MOD=7
    NEQ=8
    GTE=9
    LTE=10
    GT=11
    LT=12
    EQ=13
    AND=14
    OR=15
    NOT=16
    COMMA=17
    LPAREN=18
    RPAREN=19
    LPARENSQ=20
    RPARENSQ=21
    LEN=22
    VAL=23
    ISNAN=24
    RAND=25
    SWAP=26
    PRINT=27
    INPUT=28
    LET=29
    DIM=30
    INDEX=31
    REM=32
    IF=33
    THEN=34
    ELSE=35
    END=36
    SUBROUTINE=37
    FOR=38
    WHILE=39
    REPEAT=40
    UNTIL=41
    STEP=42
    NEXT=43
    TO=44
    CONTINUE=45
    EXIT=46
    COMMENT=47
    ID=48
    NUMBER=49
    FLOAT=50
    STRINGLITERAL=51
    DOLLAR=52
    NEWLINE=53
    WS=54

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicExpressionParser.StatContext)
            else:
                return self.getTypedRuleContext(BasicExpressionParser.StatContext,i)


        def getRuleIndex(self):
            return BasicExpressionParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = BasicExpressionParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.stat()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 13229323968643104) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(BasicExpressionParser.ExpressionContext,0)


        def NEWLINE(self):
            return self.getToken(BasicExpressionParser.NEWLINE, 0)

        def getRuleIndex(self):
            return BasicExpressionParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)




    def stat(self):

        localctx = BasicExpressionParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 16, 18, 22, 23, 24, 25, 48, 49, 50, 51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.expression(0)
                self.state = 30
                self.match(BasicExpressionParser.NEWLINE)
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.match(BasicExpressionParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BasicExpressionParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AndExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicExpressionParser.ExpressionContext,i)

        def AND(self):
            return self.getToken(BasicExpressionParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)


    class StringExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def string(self):
            return self.getTypedRuleContext(BasicExpressionParser.StringContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpr" ):
                listener.enterStringExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpr" ):
                listener.exitStringExpr(self)


    class FloatExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def float_(self):
            return self.getTypedRuleContext(BasicExpressionParser.FloatContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatExpr" ):
                listener.enterFloatExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatExpr" ):
                listener.exitFloatExpr(self)


    class IdExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def id_(self):
            return self.getTypedRuleContext(BasicExpressionParser.IdContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)


    class RelExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicExpressionParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicExpressionParser.ExpressionContext,i)

        def GTE(self):
            return self.getToken(BasicExpressionParser.GTE, 0)
        def GT(self):
            return self.getToken(BasicExpressionParser.GT, 0)
        def LTE(self):
            return self.getToken(BasicExpressionParser.LTE, 0)
        def LT(self):
            return self.getToken(BasicExpressionParser.LT, 0)
        def EQ(self):
            return self.getToken(BasicExpressionParser.EQ, 0)
        def NEQ(self):
            return self.getToken(BasicExpressionParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelExpr" ):
                listener.enterRelExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelExpr" ):
                listener.exitRelExpr(self)


    class ExpExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicExpressionParser.ExpressionContext,i)

        def EXP(self):
            return self.getToken(BasicExpressionParser.EXP, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpExpr" ):
                listener.enterExpExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpExpr" ):
                listener.exitExpExpr(self)


    class FuncExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def func(self):
            return self.getTypedRuleContext(BasicExpressionParser.FuncContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncExpr" ):
                listener.enterFuncExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncExpr" ):
                listener.exitFuncExpr(self)


    class OrExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicExpressionParser.ExpressionContext,i)

        def OR(self):
            return self.getToken(BasicExpressionParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)


    class MulDivExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicExpressionParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicExpressionParser.ExpressionContext,i)

        def MUL(self):
            return self.getToken(BasicExpressionParser.MUL, 0)
        def DIV(self):
            return self.getToken(BasicExpressionParser.DIV, 0)
        def IDIV(self):
            return self.getToken(BasicExpressionParser.IDIV, 0)
        def MOD(self):
            return self.getToken(BasicExpressionParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivExpr" ):
                listener.enterMulDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivExpr" ):
                listener.exitMulDivExpr(self)


    class ArrExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicExpressionParser.ExpressionContext,i)

        def LPARENSQ(self):
            return self.getToken(BasicExpressionParser.LPARENSQ, 0)
        def RPARENSQ(self):
            return self.getToken(BasicExpressionParser.RPARENSQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrExpr" ):
                listener.enterArrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrExpr" ):
                listener.exitArrExpr(self)


    class UnaryMinusExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(BasicExpressionParser.SUB, 0)
        def expression(self):
            return self.getTypedRuleContext(BasicExpressionParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinusExpr" ):
                listener.enterUnaryMinusExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinusExpr" ):
                listener.exitUnaryMinusExpr(self)


    class NumberExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def number(self):
            return self.getTypedRuleContext(BasicExpressionParser.NumberContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)


    class NotExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(BasicExpressionParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(BasicExpressionParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)


    class ParenExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicExpressionParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(BasicExpressionParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(BasicExpressionParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(BasicExpressionParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)


    class AddSubExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicExpressionParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicExpressionParser.ExpressionContext,i)

        def ADD(self):
            return self.getToken(BasicExpressionParser.ADD, 0)
        def SUB(self):
            return self.getToken(BasicExpressionParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BasicExpressionParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = BasicExpressionParser.UnaryMinusExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 36
                self.match(BasicExpressionParser.SUB)
                self.state = 37
                self.expression(15)
                pass
            elif token in [51]:
                localctx = BasicExpressionParser.StringExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 38
                self.string()
                pass
            elif token in [49]:
                localctx = BasicExpressionParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 39
                self.number()
                pass
            elif token in [50]:
                localctx = BasicExpressionParser.FloatExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 40
                self.float_()
                pass
            elif token in [22, 23, 24, 25]:
                localctx = BasicExpressionParser.FuncExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 41
                self.func()
                pass
            elif token in [48]:
                localctx = BasicExpressionParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 42
                self.id_()
                pass
            elif token in [18]:
                localctx = BasicExpressionParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 43
                self.match(BasicExpressionParser.LPAREN)
                self.state = 44
                self.expression(0)
                self.state = 45
                self.match(BasicExpressionParser.RPAREN)
                pass
            elif token in [16]:
                localctx = BasicExpressionParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 47
                self.match(BasicExpressionParser.NOT)
                self.state = 48
                self.expression(4)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 76
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 74
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = BasicExpressionParser.MulDivExprContext(self, BasicExpressionParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 51
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 52
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 142) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 53
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = BasicExpressionParser.AddSubExprContext(self, BasicExpressionParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 54
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 55
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==5):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 56
                        self.expression(7)
                        pass

                    elif la_ == 3:
                        localctx = BasicExpressionParser.RelExprContext(self, BasicExpressionParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 57
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 58
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16128) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 59
                        self.expression(6)
                        pass

                    elif la_ == 4:
                        localctx = BasicExpressionParser.AndExprContext(self, BasicExpressionParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 60
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 61
                        self.match(BasicExpressionParser.AND)
                        self.state = 62
                        self.expression(4)
                        pass

                    elif la_ == 5:
                        localctx = BasicExpressionParser.OrExprContext(self, BasicExpressionParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 63
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 64
                        self.match(BasicExpressionParser.OR)
                        self.state = 65
                        self.expression(3)
                        pass

                    elif la_ == 6:
                        localctx = BasicExpressionParser.ExpExprContext(self, BasicExpressionParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 66
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 67
                        self.match(BasicExpressionParser.EXP)
                        self.state = 68
                        self.expression(1)
                        pass

                    elif la_ == 7:
                        localctx = BasicExpressionParser.ArrExprContext(self, BasicExpressionParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 69
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 70
                        self.match(BasicExpressionParser.LPARENSQ)
                        self.state = 71
                        self.expression(0)
                        self.state = 72
                        self.match(BasicExpressionParser.RPARENSQ)
                        pass

             
                self.state = 78
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lenfunc(self):
            return self.getTypedRuleContext(BasicExpressionParser.LenfuncContext,0)


        def valfunc(self):
            return self.getTypedRuleContext(BasicExpressionParser.ValfuncContext,0)


        def isnanfunc(self):
            return self.getTypedRuleContext(BasicExpressionParser.IsnanfuncContext,0)


        def randfunc(self):
            return self.getTypedRuleContext(BasicExpressionParser.RandfuncContext,0)


        def getRuleIndex(self):
            return BasicExpressionParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)




    def func(self):

        localctx = BasicExpressionParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_func)
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.lenfunc()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
                self.valfunc()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 81
                self.isnanfunc()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 4)
                self.state = 82
                self.randfunc()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRINGLITERAL(self):
            return self.getToken(BasicExpressionParser.STRINGLITERAL, 0)

        def getRuleIndex(self):
            return BasicExpressionParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)




    def string(self):

        localctx = BasicExpressionParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(BasicExpressionParser.STRINGLITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(BasicExpressionParser.NUMBER, 0)

        def getRuleIndex(self):
            return BasicExpressionParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = BasicExpressionParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(BasicExpressionParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(BasicExpressionParser.FLOAT, 0)

        def getRuleIndex(self):
            return BasicExpressionParser.RULE_float

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)




    def float_(self):

        localctx = BasicExpressionParser.FloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(BasicExpressionParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BasicExpressionParser.ID, 0)

        def getRuleIndex(self):
            return BasicExpressionParser.RULE_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)




    def id_(self):

        localctx = BasicExpressionParser.IdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.match(BasicExpressionParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LenfuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEN(self):
            return self.getToken(BasicExpressionParser.LEN, 0)

        def LPAREN(self):
            return self.getToken(BasicExpressionParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(BasicExpressionParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(BasicExpressionParser.RPAREN, 0)

        def getRuleIndex(self):
            return BasicExpressionParser.RULE_lenfunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLenfunc" ):
                listener.enterLenfunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLenfunc" ):
                listener.exitLenfunc(self)




    def lenfunc(self):

        localctx = BasicExpressionParser.LenfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_lenfunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(BasicExpressionParser.LEN)
            self.state = 94
            self.match(BasicExpressionParser.LPAREN)
            self.state = 95
            self.expression(0)
            self.state = 96
            self.match(BasicExpressionParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValfuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(BasicExpressionParser.VAL, 0)

        def LPAREN(self):
            return self.getToken(BasicExpressionParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(BasicExpressionParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(BasicExpressionParser.RPAREN, 0)

        def getRuleIndex(self):
            return BasicExpressionParser.RULE_valfunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValfunc" ):
                listener.enterValfunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValfunc" ):
                listener.exitValfunc(self)




    def valfunc(self):

        localctx = BasicExpressionParser.ValfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_valfunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(BasicExpressionParser.VAL)
            self.state = 99
            self.match(BasicExpressionParser.LPAREN)
            self.state = 100
            self.expression(0)
            self.state = 101
            self.match(BasicExpressionParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IsnanfuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ISNAN(self):
            return self.getToken(BasicExpressionParser.ISNAN, 0)

        def LPAREN(self):
            return self.getToken(BasicExpressionParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(BasicExpressionParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(BasicExpressionParser.RPAREN, 0)

        def getRuleIndex(self):
            return BasicExpressionParser.RULE_isnanfunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsnanfunc" ):
                listener.enterIsnanfunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsnanfunc" ):
                listener.exitIsnanfunc(self)




    def isnanfunc(self):

        localctx = BasicExpressionParser.IsnanfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_isnanfunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(BasicExpressionParser.ISNAN)
            self.state = 104
            self.match(BasicExpressionParser.LPAREN)
            self.state = 105
            self.expression(0)
            self.state = 106
            self.match(BasicExpressionParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RandfuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RAND(self):
            return self.getToken(BasicExpressionParser.RAND, 0)

        def LPAREN(self):
            return self.getToken(BasicExpressionParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicExpressionParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicExpressionParser.ExpressionContext,i)


        def COMMA(self):
            return self.getToken(BasicExpressionParser.COMMA, 0)

        def RPAREN(self):
            return self.getToken(BasicExpressionParser.RPAREN, 0)

        def getRuleIndex(self):
            return BasicExpressionParser.RULE_randfunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRandfunc" ):
                listener.enterRandfunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRandfunc" ):
                listener.exitRandfunc(self)




    def randfunc(self):

        localctx = BasicExpressionParser.RandfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_randfunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(BasicExpressionParser.RAND)
            self.state = 109
            self.match(BasicExpressionParser.LPAREN)
            self.state = 110
            self.expression(0)
            self.state = 111
            self.match(BasicExpressionParser.COMMA)
            self.state = 112
            self.expression(0)
            self.state = 113
            self.match(BasicExpressionParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 1)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 8)
         




