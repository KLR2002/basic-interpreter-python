# Generated from ./BasicLanguage.g4 by ANTLR 4.13.1
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
        4,1,54,368,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        3,1,84,8,1,1,2,1,2,4,2,88,8,2,11,2,12,2,89,1,2,3,2,93,8,2,5,2,95,
        8,2,10,2,12,2,98,9,2,1,3,3,3,101,8,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,
        1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,3,6,121,8,6,1,7,1,7,
        1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,5,11,137,
        8,11,10,11,12,11,140,9,11,1,11,1,11,4,11,144,8,11,11,11,12,11,145,
        1,11,1,11,5,11,150,8,11,10,11,12,11,153,9,11,1,11,3,11,156,8,11,
        1,11,1,11,1,12,1,12,1,12,1,12,5,12,164,8,12,10,12,12,12,167,9,12,
        1,12,1,12,4,12,171,8,12,11,12,12,12,172,1,12,1,12,1,13,1,13,4,13,
        179,8,13,11,13,12,13,180,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,
        5,14,191,8,14,10,14,12,14,194,9,14,5,14,196,8,14,10,14,12,14,199,
        9,14,1,14,1,14,4,14,203,8,14,11,14,12,14,204,1,14,1,14,1,14,1,15,
        1,15,1,15,1,15,1,15,5,15,215,8,15,10,15,12,15,218,9,15,5,15,220,
        8,15,10,15,12,15,223,9,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,3,16,235,8,16,1,16,4,16,238,8,16,11,16,12,16,239,1,16,
        1,16,1,16,1,17,1,17,1,17,4,17,248,8,17,11,17,12,17,249,1,17,1,17,
        1,17,1,18,1,18,4,18,257,8,18,11,18,12,18,258,1,18,1,18,5,18,263,
        8,18,10,18,12,18,266,9,18,1,18,1,18,1,18,1,19,1,19,1,20,1,20,1,21,
        1,21,1,21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,3,22,286,8,22,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,3,23,302,8,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,
        1,23,5,23,327,8,23,10,23,12,23,330,9,23,1,24,1,24,1,24,1,24,3,24,
        336,8,24,1,25,1,25,1,26,1,26,1,27,1,27,1,28,1,28,1,29,1,29,1,29,
        1,29,1,29,1,30,1,30,1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,32,
        1,32,1,32,1,32,1,32,1,32,1,32,1,32,0,1,46,33,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,
        60,62,64,0,3,2,0,1,3,7,7,1,0,4,5,1,0,8,13,387,0,66,1,0,0,0,2,83,
        1,0,0,0,4,96,1,0,0,0,6,100,1,0,0,0,8,106,1,0,0,0,10,110,1,0,0,0,
        12,118,1,0,0,0,14,122,1,0,0,0,16,124,1,0,0,0,18,126,1,0,0,0,20,129,
        1,0,0,0,22,133,1,0,0,0,24,159,1,0,0,0,26,176,1,0,0,0,28,184,1,0,
        0,0,30,209,1,0,0,0,32,226,1,0,0,0,34,244,1,0,0,0,36,254,1,0,0,0,
        38,270,1,0,0,0,40,272,1,0,0,0,42,274,1,0,0,0,44,285,1,0,0,0,46,301,
        1,0,0,0,48,335,1,0,0,0,50,337,1,0,0,0,52,339,1,0,0,0,54,341,1,0,
        0,0,56,343,1,0,0,0,58,345,1,0,0,0,60,350,1,0,0,0,62,355,1,0,0,0,
        64,360,1,0,0,0,66,67,3,4,2,0,67,68,5,0,0,1,68,1,1,0,0,0,69,84,3,
        6,3,0,70,84,3,8,4,0,71,84,3,10,5,0,72,84,3,18,9,0,73,84,3,20,10,
        0,74,84,3,22,11,0,75,84,3,28,14,0,76,84,3,32,16,0,77,84,3,34,17,
        0,78,84,3,36,18,0,79,84,3,38,19,0,80,84,3,40,20,0,81,84,3,42,21,
        0,82,84,5,47,0,0,83,69,1,0,0,0,83,70,1,0,0,0,83,71,1,0,0,0,83,72,
        1,0,0,0,83,73,1,0,0,0,83,74,1,0,0,0,83,75,1,0,0,0,83,76,1,0,0,0,
        83,77,1,0,0,0,83,78,1,0,0,0,83,79,1,0,0,0,83,80,1,0,0,0,83,81,1,
        0,0,0,83,82,1,0,0,0,84,3,1,0,0,0,85,92,3,2,1,0,86,88,5,53,0,0,87,
        86,1,0,0,0,88,89,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,93,1,0,0,
        0,91,93,5,0,0,1,92,87,1,0,0,0,92,91,1,0,0,0,93,95,1,0,0,0,94,85,
        1,0,0,0,95,98,1,0,0,0,96,94,1,0,0,0,96,97,1,0,0,0,97,5,1,0,0,0,98,
        96,1,0,0,0,99,101,5,29,0,0,100,99,1,0,0,0,100,101,1,0,0,0,101,102,
        1,0,0,0,102,103,3,12,6,0,103,104,5,13,0,0,104,105,3,46,23,0,105,
        7,1,0,0,0,106,107,5,30,0,0,107,108,3,12,6,0,108,109,3,46,23,0,109,
        9,1,0,0,0,110,111,5,31,0,0,111,112,3,14,7,0,112,113,5,20,0,0,113,
        114,3,46,23,0,114,115,5,21,0,0,115,116,5,13,0,0,116,117,3,46,23,
        0,117,11,1,0,0,0,118,120,3,14,7,0,119,121,3,16,8,0,120,119,1,0,0,
        0,120,121,1,0,0,0,121,13,1,0,0,0,122,123,5,48,0,0,123,15,1,0,0,0,
        124,125,5,52,0,0,125,17,1,0,0,0,126,127,5,27,0,0,127,128,3,46,23,
        0,128,19,1,0,0,0,129,130,5,28,0,0,130,131,3,50,25,0,131,132,3,12,
        6,0,132,21,1,0,0,0,133,134,5,33,0,0,134,138,3,46,23,0,135,137,5,
        53,0,0,136,135,1,0,0,0,137,140,1,0,0,0,138,136,1,0,0,0,138,139,1,
        0,0,0,139,141,1,0,0,0,140,138,1,0,0,0,141,143,5,34,0,0,142,144,5,
        53,0,0,143,142,1,0,0,0,144,145,1,0,0,0,145,143,1,0,0,0,145,146,1,
        0,0,0,146,147,1,0,0,0,147,151,3,4,2,0,148,150,3,24,12,0,149,148,
        1,0,0,0,150,153,1,0,0,0,151,149,1,0,0,0,151,152,1,0,0,0,152,155,
        1,0,0,0,153,151,1,0,0,0,154,156,3,26,13,0,155,154,1,0,0,0,155,156,
        1,0,0,0,156,157,1,0,0,0,157,158,5,36,0,0,158,23,1,0,0,0,159,160,
        5,35,0,0,160,161,5,33,0,0,161,165,3,46,23,0,162,164,5,53,0,0,163,
        162,1,0,0,0,164,167,1,0,0,0,165,163,1,0,0,0,165,166,1,0,0,0,166,
        168,1,0,0,0,167,165,1,0,0,0,168,170,5,34,0,0,169,171,5,53,0,0,170,
        169,1,0,0,0,171,172,1,0,0,0,172,170,1,0,0,0,172,173,1,0,0,0,173,
        174,1,0,0,0,174,175,3,4,2,0,175,25,1,0,0,0,176,178,5,35,0,0,177,
        179,5,53,0,0,178,177,1,0,0,0,179,180,1,0,0,0,180,178,1,0,0,0,180,
        181,1,0,0,0,181,182,1,0,0,0,182,183,3,4,2,0,183,27,1,0,0,0,184,185,
        5,37,0,0,185,186,5,48,0,0,186,197,5,18,0,0,187,192,5,48,0,0,188,
        189,5,17,0,0,189,191,5,48,0,0,190,188,1,0,0,0,191,194,1,0,0,0,192,
        190,1,0,0,0,192,193,1,0,0,0,193,196,1,0,0,0,194,192,1,0,0,0,195,
        187,1,0,0,0,196,199,1,0,0,0,197,195,1,0,0,0,197,198,1,0,0,0,198,
        200,1,0,0,0,199,197,1,0,0,0,200,202,5,19,0,0,201,203,5,53,0,0,202,
        201,1,0,0,0,203,204,1,0,0,0,204,202,1,0,0,0,204,205,1,0,0,0,205,
        206,1,0,0,0,206,207,3,4,2,0,207,208,5,36,0,0,208,29,1,0,0,0,209,
        210,5,48,0,0,210,221,5,18,0,0,211,216,3,46,23,0,212,213,5,17,0,0,
        213,215,3,46,23,0,214,212,1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,
        0,216,217,1,0,0,0,217,220,1,0,0,0,218,216,1,0,0,0,219,211,1,0,0,
        0,220,223,1,0,0,0,221,219,1,0,0,0,221,222,1,0,0,0,222,224,1,0,0,
        0,223,221,1,0,0,0,224,225,5,19,0,0,225,31,1,0,0,0,226,227,5,38,0,
        0,227,228,3,12,6,0,228,229,5,13,0,0,229,230,3,46,23,0,230,231,5,
        44,0,0,231,234,3,46,23,0,232,233,5,42,0,0,233,235,3,46,23,0,234,
        232,1,0,0,0,234,235,1,0,0,0,235,237,1,0,0,0,236,238,5,53,0,0,237,
        236,1,0,0,0,238,239,1,0,0,0,239,237,1,0,0,0,239,240,1,0,0,0,240,
        241,1,0,0,0,241,242,3,4,2,0,242,243,5,43,0,0,243,33,1,0,0,0,244,
        245,5,39,0,0,245,247,3,46,23,0,246,248,5,53,0,0,247,246,1,0,0,0,
        248,249,1,0,0,0,249,247,1,0,0,0,249,250,1,0,0,0,250,251,1,0,0,0,
        251,252,3,4,2,0,252,253,5,36,0,0,253,35,1,0,0,0,254,256,5,40,0,0,
        255,257,5,53,0,0,256,255,1,0,0,0,257,258,1,0,0,0,258,256,1,0,0,0,
        258,259,1,0,0,0,259,260,1,0,0,0,260,264,3,4,2,0,261,263,5,53,0,0,
        262,261,1,0,0,0,263,266,1,0,0,0,264,262,1,0,0,0,264,265,1,0,0,0,
        265,267,1,0,0,0,266,264,1,0,0,0,267,268,5,41,0,0,268,269,3,46,23,
        0,269,37,1,0,0,0,270,271,5,45,0,0,271,39,1,0,0,0,272,273,5,46,0,
        0,273,41,1,0,0,0,274,275,5,26,0,0,275,276,5,18,0,0,276,277,3,46,
        23,0,277,278,5,17,0,0,278,279,3,46,23,0,279,280,5,19,0,0,280,43,
        1,0,0,0,281,282,3,46,23,0,282,283,5,53,0,0,283,286,1,0,0,0,284,286,
        5,53,0,0,285,281,1,0,0,0,285,284,1,0,0,0,286,45,1,0,0,0,287,288,
        6,23,-1,0,288,289,5,5,0,0,289,302,3,46,23,15,290,302,3,50,25,0,291,
        302,3,52,26,0,292,302,3,54,27,0,293,302,3,48,24,0,294,302,3,56,28,
        0,295,296,5,18,0,0,296,297,3,46,23,0,297,298,5,19,0,0,298,302,1,
        0,0,0,299,300,5,16,0,0,300,302,3,46,23,4,301,287,1,0,0,0,301,290,
        1,0,0,0,301,291,1,0,0,0,301,292,1,0,0,0,301,293,1,0,0,0,301,294,
        1,0,0,0,301,295,1,0,0,0,301,299,1,0,0,0,302,328,1,0,0,0,303,304,
        10,7,0,0,304,305,7,0,0,0,305,327,3,46,23,8,306,307,10,6,0,0,307,
        308,7,1,0,0,308,327,3,46,23,7,309,310,10,5,0,0,310,311,7,2,0,0,311,
        327,3,46,23,6,312,313,10,3,0,0,313,314,5,14,0,0,314,327,3,46,23,
        4,315,316,10,2,0,0,316,317,5,15,0,0,317,327,3,46,23,3,318,319,10,
        1,0,0,319,320,5,6,0,0,320,327,3,46,23,1,321,322,10,8,0,0,322,323,
        5,20,0,0,323,324,3,46,23,0,324,325,5,21,0,0,325,327,1,0,0,0,326,
        303,1,0,0,0,326,306,1,0,0,0,326,309,1,0,0,0,326,312,1,0,0,0,326,
        315,1,0,0,0,326,318,1,0,0,0,326,321,1,0,0,0,327,330,1,0,0,0,328,
        326,1,0,0,0,328,329,1,0,0,0,329,47,1,0,0,0,330,328,1,0,0,0,331,336,
        3,58,29,0,332,336,3,60,30,0,333,336,3,62,31,0,334,336,3,64,32,0,
        335,331,1,0,0,0,335,332,1,0,0,0,335,333,1,0,0,0,335,334,1,0,0,0,
        336,49,1,0,0,0,337,338,5,51,0,0,338,51,1,0,0,0,339,340,5,49,0,0,
        340,53,1,0,0,0,341,342,5,50,0,0,342,55,1,0,0,0,343,344,5,48,0,0,
        344,57,1,0,0,0,345,346,5,22,0,0,346,347,5,18,0,0,347,348,3,46,23,
        0,348,349,5,19,0,0,349,59,1,0,0,0,350,351,5,23,0,0,351,352,5,18,
        0,0,352,353,3,46,23,0,353,354,5,19,0,0,354,61,1,0,0,0,355,356,5,
        24,0,0,356,357,5,18,0,0,357,358,3,46,23,0,358,359,5,19,0,0,359,63,
        1,0,0,0,360,361,5,25,0,0,361,362,5,18,0,0,362,363,3,46,23,0,363,
        364,5,17,0,0,364,365,3,46,23,0,365,366,5,19,0,0,366,65,1,0,0,0,28,
        83,89,92,96,100,120,138,145,151,155,165,172,180,192,197,204,216,
        221,234,239,249,258,264,285,301,326,328,335
    ]

class BasicLanguageParser ( Parser ):

    grammarFileName = "BasicLanguage.g4"

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
    RULE_statement = 1
    RULE_block = 2
    RULE_letStmt = 3
    RULE_arrStmt = 4
    RULE_arrElementStmt = 5
    RULE_vardecl = 6
    RULE_varname = 7
    RULE_varsuffix = 8
    RULE_printStmt = 9
    RULE_inputStmt = 10
    RULE_ifStmt = 11
    RULE_elifStmt = 12
    RULE_elseStmt = 13
    RULE_subStmt = 14
    RULE_subCall = 15
    RULE_forStmt = 16
    RULE_whileStmt = 17
    RULE_repeatStmt = 18
    RULE_continueStmt = 19
    RULE_exitStmt = 20
    RULE_swapFunc = 21
    RULE_stat = 22
    RULE_expression = 23
    RULE_func = 24
    RULE_string = 25
    RULE_number = 26
    RULE_float = 27
    RULE_id = 28
    RULE_lenfunc = 29
    RULE_valfunc = 30
    RULE_isnanfunc = 31
    RULE_randfunc = 32

    ruleNames =  [ "prog", "statement", "block", "letStmt", "arrStmt", "arrElementStmt", 
                   "vardecl", "varname", "varsuffix", "printStmt", "inputStmt", 
                   "ifStmt", "elifStmt", "elseStmt", "subStmt", "subCall", 
                   "forStmt", "whileStmt", "repeatStmt", "continueStmt", 
                   "exitStmt", "swapFunc", "stat", "expression", "func", 
                   "string", "number", "float", "id", "lenfunc", "valfunc", 
                   "isnanfunc", "randfunc" ]

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

        def block(self):
            return self.getTypedRuleContext(BasicLanguageParser.BlockContext,0)


        def EOF(self):
            return self.getToken(BasicLanguageParser.EOF, 0)

        def getRuleIndex(self):
            return BasicLanguageParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = BasicLanguageParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.block()
            self.state = 67
            self.match(BasicLanguageParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def letStmt(self):
            return self.getTypedRuleContext(BasicLanguageParser.LetStmtContext,0)


        def arrStmt(self):
            return self.getTypedRuleContext(BasicLanguageParser.ArrStmtContext,0)


        def arrElementStmt(self):
            return self.getTypedRuleContext(BasicLanguageParser.ArrElementStmtContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(BasicLanguageParser.PrintStmtContext,0)


        def inputStmt(self):
            return self.getTypedRuleContext(BasicLanguageParser.InputStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(BasicLanguageParser.IfStmtContext,0)


        def subStmt(self):
            return self.getTypedRuleContext(BasicLanguageParser.SubStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(BasicLanguageParser.ForStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(BasicLanguageParser.WhileStmtContext,0)


        def repeatStmt(self):
            return self.getTypedRuleContext(BasicLanguageParser.RepeatStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(BasicLanguageParser.ContinueStmtContext,0)


        def exitStmt(self):
            return self.getTypedRuleContext(BasicLanguageParser.ExitStmtContext,0)


        def swapFunc(self):
            return self.getTypedRuleContext(BasicLanguageParser.SwapFuncContext,0)


        def COMMENT(self):
            return self.getToken(BasicLanguageParser.COMMENT, 0)

        def getRuleIndex(self):
            return BasicLanguageParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BasicLanguageParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29, 48]:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.letStmt()
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.arrStmt()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 3)
                self.state = 71
                self.arrElementStmt()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.printStmt()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 5)
                self.state = 73
                self.inputStmt()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 6)
                self.state = 74
                self.ifStmt()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 7)
                self.state = 75
                self.subStmt()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 8)
                self.state = 76
                self.forStmt()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 9)
                self.state = 77
                self.whileStmt()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 10)
                self.state = 78
                self.repeatStmt()
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 11)
                self.state = 79
                self.continueStmt()
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 12)
                self.state = 80
                self.exitStmt()
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 13)
                self.state = 81
                self.swapFunc()
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 14)
                self.state = 82
                self.match(BasicLanguageParser.COMMENT)
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


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicLanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(BasicLanguageParser.StatementContext,i)


        def EOF(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLanguageParser.EOF)
            else:
                return self.getToken(BasicLanguageParser.EOF, i)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLanguageParser.NEWLINE)
            else:
                return self.getToken(BasicLanguageParser.NEWLINE, i)

        def getRuleIndex(self):
            return BasicLanguageParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = BasicLanguageParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 529839983427584) != 0):
                self.state = 85
                self.statement()
                self.state = 92
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [53]:
                    self.state = 87 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 86
                            self.match(BasicLanguageParser.NEWLINE)

                        else:
                            raise NoViableAltException(self)
                        self.state = 89 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

                    pass
                elif token in [-1]:
                    self.state = 91
                    self.match(BasicLanguageParser.EOF)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LetStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(BasicLanguageParser.VardeclContext,0)


        def EQ(self):
            return self.getToken(BasicLanguageParser.EQ, 0)

        def expression(self):
            return self.getTypedRuleContext(BasicLanguageParser.ExpressionContext,0)


        def LET(self):
            return self.getToken(BasicLanguageParser.LET, 0)

        def getRuleIndex(self):
            return BasicLanguageParser.RULE_letStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLetStmt" ):
                listener.enterLetStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLetStmt" ):
                listener.exitLetStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLetStmt" ):
                return visitor.visitLetStmt(self)
            else:
                return visitor.visitChildren(self)




    def letStmt(self):

        localctx = BasicLanguageParser.LetStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_letStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 99
                self.match(BasicLanguageParser.LET)


            self.state = 102
            self.vardecl()
            self.state = 103
            self.match(BasicLanguageParser.EQ)
            self.state = 104
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DIM(self):
            return self.getToken(BasicLanguageParser.DIM, 0)

        def vardecl(self):
            return self.getTypedRuleContext(BasicLanguageParser.VardeclContext,0)


        def expression(self):
            return self.getTypedRuleContext(BasicLanguageParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BasicLanguageParser.RULE_arrStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrStmt" ):
                listener.enterArrStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrStmt" ):
                listener.exitArrStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrStmt" ):
                return visitor.visitArrStmt(self)
            else:
                return visitor.visitChildren(self)




    def arrStmt(self):

        localctx = BasicLanguageParser.ArrStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arrStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(BasicLanguageParser.DIM)
            self.state = 107
            self.vardecl()
            self.state = 108
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrElementStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INDEX(self):
            return self.getToken(BasicLanguageParser.INDEX, 0)

        def varname(self):
            return self.getTypedRuleContext(BasicLanguageParser.VarnameContext,0)


        def LPARENSQ(self):
            return self.getToken(BasicLanguageParser.LPARENSQ, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicLanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicLanguageParser.ExpressionContext,i)


        def RPARENSQ(self):
            return self.getToken(BasicLanguageParser.RPARENSQ, 0)

        def EQ(self):
            return self.getToken(BasicLanguageParser.EQ, 0)

        def getRuleIndex(self):
            return BasicLanguageParser.RULE_arrElementStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrElementStmt" ):
                listener.enterArrElementStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrElementStmt" ):
                listener.exitArrElementStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrElementStmt" ):
                return visitor.visitArrElementStmt(self)
            else:
                return visitor.visitChildren(self)




    def arrElementStmt(self):

        localctx = BasicLanguageParser.ArrElementStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_arrElementStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(BasicLanguageParser.INDEX)
            self.state = 111
            self.varname()
            self.state = 112
            self.match(BasicLanguageParser.LPARENSQ)
            self.state = 113
            self.expression(0)
            self.state = 114
            self.match(BasicLanguageParser.RPARENSQ)
            self.state = 115
            self.match(BasicLanguageParser.EQ)
            self.state = 116
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varname(self):
            return self.getTypedRuleContext(BasicLanguageParser.VarnameContext,0)


        def varsuffix(self):
            return self.getTypedRuleContext(BasicLanguageParser.VarsuffixContext,0)


        def getRuleIndex(self):
            return BasicLanguageParser.RULE_vardecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVardecl" ):
                listener.enterVardecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVardecl" ):
                listener.exitVardecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = BasicLanguageParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.varname()
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==52:
                self.state = 119
                self.varsuffix()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarnameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BasicLanguageParser.ID, 0)

        def getRuleIndex(self):
            return BasicLanguageParser.RULE_varname

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarname" ):
                listener.enterVarname(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarname" ):
                listener.exitVarname(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarname" ):
                return visitor.visitVarname(self)
            else:
                return visitor.visitChildren(self)




    def varname(self):

        localctx = BasicLanguageParser.VarnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_varname)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(BasicLanguageParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarsuffixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLAR(self):
            return self.getToken(BasicLanguageParser.DOLLAR, 0)

        def getRuleIndex(self):
            return BasicLanguageParser.RULE_varsuffix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarsuffix" ):
                listener.enterVarsuffix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarsuffix" ):
                listener.exitVarsuffix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarsuffix" ):
                return visitor.visitVarsuffix(self)
            else:
                return visitor.visitChildren(self)




    def varsuffix(self):

        localctx = BasicLanguageParser.VarsuffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_varsuffix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(BasicLanguageParser.DOLLAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(BasicLanguageParser.PRINT, 0)

        def expression(self):
            return self.getTypedRuleContext(BasicLanguageParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BasicLanguageParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = BasicLanguageParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(BasicLanguageParser.PRINT)
            self.state = 127
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INPUT(self):
            return self.getToken(BasicLanguageParser.INPUT, 0)

        def string(self):
            return self.getTypedRuleContext(BasicLanguageParser.StringContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(BasicLanguageParser.VardeclContext,0)


        def getRuleIndex(self):
            return BasicLanguageParser.RULE_inputStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInputStmt" ):
                listener.enterInputStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInputStmt" ):
                listener.exitInputStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInputStmt" ):
                return visitor.visitInputStmt(self)
            else:
                return visitor.visitChildren(self)




    def inputStmt(self):

        localctx = BasicLanguageParser.InputStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_inputStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(BasicLanguageParser.INPUT)
            self.state = 130
            self.string()
            self.state = 131
            self.vardecl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BasicLanguageParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(BasicLanguageParser.ExpressionContext,0)


        def THEN(self):
            return self.getToken(BasicLanguageParser.THEN, 0)

        def block(self):
            return self.getTypedRuleContext(BasicLanguageParser.BlockContext,0)


        def END(self):
            return self.getToken(BasicLanguageParser.END, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLanguageParser.NEWLINE)
            else:
                return self.getToken(BasicLanguageParser.NEWLINE, i)

        def elifStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicLanguageParser.ElifStmtContext)
            else:
                return self.getTypedRuleContext(BasicLanguageParser.ElifStmtContext,i)


        def elseStmt(self):
            return self.getTypedRuleContext(BasicLanguageParser.ElseStmtContext,0)


        def getRuleIndex(self):
            return BasicLanguageParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = BasicLanguageParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.match(BasicLanguageParser.IF)
            self.state = 134
            self.expression(0)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==53:
                self.state = 135
                self.match(BasicLanguageParser.NEWLINE)
                self.state = 140
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 141
            self.match(BasicLanguageParser.THEN)
            self.state = 143 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 142
                self.match(BasicLanguageParser.NEWLINE)
                self.state = 145 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==53):
                    break

            self.state = 147
            self.block()
            self.state = 151
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 148
                    self.elifStmt() 
                self.state = 153
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 154
                self.elseStmt()


            self.state = 157
            self.match(BasicLanguageParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(BasicLanguageParser.ELSE, 0)

        def IF(self):
            return self.getToken(BasicLanguageParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(BasicLanguageParser.ExpressionContext,0)


        def THEN(self):
            return self.getToken(BasicLanguageParser.THEN, 0)

        def block(self):
            return self.getTypedRuleContext(BasicLanguageParser.BlockContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLanguageParser.NEWLINE)
            else:
                return self.getToken(BasicLanguageParser.NEWLINE, i)

        def getRuleIndex(self):
            return BasicLanguageParser.RULE_elifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElifStmt" ):
                listener.enterElifStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElifStmt" ):
                listener.exitElifStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifStmt" ):
                return visitor.visitElifStmt(self)
            else:
                return visitor.visitChildren(self)




    def elifStmt(self):

        localctx = BasicLanguageParser.ElifStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_elifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(BasicLanguageParser.ELSE)
            self.state = 160
            self.match(BasicLanguageParser.IF)
            self.state = 161
            self.expression(0)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==53:
                self.state = 162
                self.match(BasicLanguageParser.NEWLINE)
                self.state = 167
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 168
            self.match(BasicLanguageParser.THEN)
            self.state = 170 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 169
                self.match(BasicLanguageParser.NEWLINE)
                self.state = 172 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==53):
                    break

            self.state = 174
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(BasicLanguageParser.ELSE, 0)

        def block(self):
            return self.getTypedRuleContext(BasicLanguageParser.BlockContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLanguageParser.NEWLINE)
            else:
                return self.getToken(BasicLanguageParser.NEWLINE, i)

        def getRuleIndex(self):
            return BasicLanguageParser.RULE_elseStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseStmt" ):
                listener.enterElseStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseStmt" ):
                listener.exitElseStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseStmt" ):
                return visitor.visitElseStmt(self)
            else:
                return visitor.visitChildren(self)




    def elseStmt(self):

        localctx = BasicLanguageParser.ElseStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_elseStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(BasicLanguageParser.ELSE)
            self.state = 178 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 177
                self.match(BasicLanguageParser.NEWLINE)
                self.state = 180 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==53):
                    break

            self.state = 182
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUBROUTINE(self):
            return self.getToken(BasicLanguageParser.SUBROUTINE, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLanguageParser.ID)
            else:
                return self.getToken(BasicLanguageParser.ID, i)

        def LPAREN(self):
            return self.getToken(BasicLanguageParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(BasicLanguageParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(BasicLanguageParser.BlockContext,0)


        def END(self):
            return self.getToken(BasicLanguageParser.END, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLanguageParser.NEWLINE)
            else:
                return self.getToken(BasicLanguageParser.NEWLINE, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLanguageParser.COMMA)
            else:
                return self.getToken(BasicLanguageParser.COMMA, i)

        def getRuleIndex(self):
            return BasicLanguageParser.RULE_subStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubStmt" ):
                listener.enterSubStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubStmt" ):
                listener.exitSubStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubStmt" ):
                return visitor.visitSubStmt(self)
            else:
                return visitor.visitChildren(self)




    def subStmt(self):

        localctx = BasicLanguageParser.SubStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_subStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(BasicLanguageParser.SUBROUTINE)
            self.state = 185
            self.match(BasicLanguageParser.ID)
            self.state = 186
            self.match(BasicLanguageParser.LPAREN)
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 187
                self.match(BasicLanguageParser.ID)
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==17:
                    self.state = 188
                    self.match(BasicLanguageParser.COMMA)
                    self.state = 189
                    self.match(BasicLanguageParser.ID)
                    self.state = 194
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 200
            self.match(BasicLanguageParser.RPAREN)
            self.state = 202 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 201
                self.match(BasicLanguageParser.NEWLINE)
                self.state = 204 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==53):
                    break

            self.state = 206
            self.block()
            self.state = 207
            self.match(BasicLanguageParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BasicLanguageParser.ID, 0)

        def LPAREN(self):
            return self.getToken(BasicLanguageParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(BasicLanguageParser.RPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicLanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicLanguageParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLanguageParser.COMMA)
            else:
                return self.getToken(BasicLanguageParser.COMMA, i)

        def getRuleIndex(self):
            return BasicLanguageParser.RULE_subCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubCall" ):
                listener.enterSubCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubCall" ):
                listener.exitSubCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubCall" ):
                return visitor.visitSubCall(self)
            else:
                return visitor.visitChildren(self)




    def subCall(self):

        localctx = BasicLanguageParser.SubCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_subCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(BasicLanguageParser.ID)
            self.state = 210
            self.match(BasicLanguageParser.LPAREN)
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4222124713902112) != 0):
                self.state = 211
                self.expression(0)
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==17:
                    self.state = 212
                    self.match(BasicLanguageParser.COMMA)
                    self.state = 213
                    self.expression(0)
                    self.state = 218
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 224
            self.match(BasicLanguageParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BasicLanguageParser.FOR, 0)

        def vardecl(self):
            return self.getTypedRuleContext(BasicLanguageParser.VardeclContext,0)


        def EQ(self):
            return self.getToken(BasicLanguageParser.EQ, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicLanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicLanguageParser.ExpressionContext,i)


        def TO(self):
            return self.getToken(BasicLanguageParser.TO, 0)

        def block(self):
            return self.getTypedRuleContext(BasicLanguageParser.BlockContext,0)


        def NEXT(self):
            return self.getToken(BasicLanguageParser.NEXT, 0)

        def STEP(self):
            return self.getToken(BasicLanguageParser.STEP, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLanguageParser.NEWLINE)
            else:
                return self.getToken(BasicLanguageParser.NEWLINE, i)

        def getRuleIndex(self):
            return BasicLanguageParser.RULE_forStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStmt" ):
                listener.enterForStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStmt" ):
                listener.exitForStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = BasicLanguageParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(BasicLanguageParser.FOR)
            self.state = 227
            self.vardecl()
            self.state = 228
            self.match(BasicLanguageParser.EQ)
            self.state = 229
            self.expression(0)
            self.state = 230
            self.match(BasicLanguageParser.TO)
            self.state = 231
            self.expression(0)
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 232
                self.match(BasicLanguageParser.STEP)
                self.state = 233
                self.expression(0)


            self.state = 237 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 236
                self.match(BasicLanguageParser.NEWLINE)
                self.state = 239 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==53):
                    break

            self.state = 241
            self.block()
            self.state = 242
            self.match(BasicLanguageParser.NEXT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BasicLanguageParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(BasicLanguageParser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(BasicLanguageParser.BlockContext,0)


        def END(self):
            return self.getToken(BasicLanguageParser.END, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLanguageParser.NEWLINE)
            else:
                return self.getToken(BasicLanguageParser.NEWLINE, i)

        def getRuleIndex(self):
            return BasicLanguageParser.RULE_whileStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = BasicLanguageParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_whileStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.match(BasicLanguageParser.WHILE)
            self.state = 245
            self.expression(0)
            self.state = 247 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 246
                self.match(BasicLanguageParser.NEWLINE)
                self.state = 249 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==53):
                    break

            self.state = 251
            self.block()
            self.state = 252
            self.match(BasicLanguageParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepeatStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPEAT(self):
            return self.getToken(BasicLanguageParser.REPEAT, 0)

        def block(self):
            return self.getTypedRuleContext(BasicLanguageParser.BlockContext,0)


        def UNTIL(self):
            return self.getToken(BasicLanguageParser.UNTIL, 0)

        def expression(self):
            return self.getTypedRuleContext(BasicLanguageParser.ExpressionContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(BasicLanguageParser.NEWLINE)
            else:
                return self.getToken(BasicLanguageParser.NEWLINE, i)

        def getRuleIndex(self):
            return BasicLanguageParser.RULE_repeatStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeatStmt" ):
                listener.enterRepeatStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeatStmt" ):
                listener.exitRepeatStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepeatStmt" ):
                return visitor.visitRepeatStmt(self)
            else:
                return visitor.visitChildren(self)




    def repeatStmt(self):

        localctx = BasicLanguageParser.RepeatStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_repeatStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(BasicLanguageParser.REPEAT)
            self.state = 256 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 255
                    self.match(BasicLanguageParser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 258 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

            self.state = 260
            self.block()
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==53:
                self.state = 261
                self.match(BasicLanguageParser.NEWLINE)
                self.state = 266
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 267
            self.match(BasicLanguageParser.UNTIL)
            self.state = 268
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BasicLanguageParser.CONTINUE, 0)

        def getRuleIndex(self):
            return BasicLanguageParser.RULE_continueStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStmt" ):
                listener.enterContinueStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStmt" ):
                listener.exitContinueStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStmt" ):
                return visitor.visitContinueStmt(self)
            else:
                return visitor.visitChildren(self)




    def continueStmt(self):

        localctx = BasicLanguageParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(BasicLanguageParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExitStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXIT(self):
            return self.getToken(BasicLanguageParser.EXIT, 0)

        def getRuleIndex(self):
            return BasicLanguageParser.RULE_exitStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExitStmt" ):
                listener.enterExitStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExitStmt" ):
                listener.exitExitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExitStmt" ):
                return visitor.visitExitStmt(self)
            else:
                return visitor.visitChildren(self)




    def exitStmt(self):

        localctx = BasicLanguageParser.ExitStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_exitStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.match(BasicLanguageParser.EXIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwapFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWAP(self):
            return self.getToken(BasicLanguageParser.SWAP, 0)

        def LPAREN(self):
            return self.getToken(BasicLanguageParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicLanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicLanguageParser.ExpressionContext,i)


        def COMMA(self):
            return self.getToken(BasicLanguageParser.COMMA, 0)

        def RPAREN(self):
            return self.getToken(BasicLanguageParser.RPAREN, 0)

        def getRuleIndex(self):
            return BasicLanguageParser.RULE_swapFunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwapFunc" ):
                listener.enterSwapFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwapFunc" ):
                listener.exitSwapFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwapFunc" ):
                return visitor.visitSwapFunc(self)
            else:
                return visitor.visitChildren(self)




    def swapFunc(self):

        localctx = BasicLanguageParser.SwapFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_swapFunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(BasicLanguageParser.SWAP)
            self.state = 275
            self.match(BasicLanguageParser.LPAREN)
            self.state = 276
            self.expression(0)
            self.state = 277
            self.match(BasicLanguageParser.COMMA)
            self.state = 278
            self.expression(0)
            self.state = 279
            self.match(BasicLanguageParser.RPAREN)
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
            return self.getTypedRuleContext(BasicLanguageParser.ExpressionContext,0)


        def NEWLINE(self):
            return self.getToken(BasicLanguageParser.NEWLINE, 0)

        def getRuleIndex(self):
            return BasicLanguageParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = BasicLanguageParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_stat)
        try:
            self.state = 285
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 16, 18, 22, 23, 24, 25, 48, 49, 50, 51]:
                self.enterOuterAlt(localctx, 1)
                self.state = 281
                self.expression(0)
                self.state = 282
                self.match(BasicLanguageParser.NEWLINE)
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 2)
                self.state = 284
                self.match(BasicLanguageParser.NEWLINE)
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
            return BasicLanguageParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AndExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicLanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicLanguageParser.ExpressionContext,i)

        def AND(self):
            return self.getToken(BasicLanguageParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndExpr" ):
                return visitor.visitAndExpr(self)
            else:
                return visitor.visitChildren(self)


    class StringExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def string(self):
            return self.getTypedRuleContext(BasicLanguageParser.StringContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpr" ):
                listener.enterStringExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpr" ):
                listener.exitStringExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpr" ):
                return visitor.visitStringExpr(self)
            else:
                return visitor.visitChildren(self)


    class FloatExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def float_(self):
            return self.getTypedRuleContext(BasicLanguageParser.FloatContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatExpr" ):
                listener.enterFloatExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatExpr" ):
                listener.exitFloatExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatExpr" ):
                return visitor.visitFloatExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def id_(self):
            return self.getTypedRuleContext(BasicLanguageParser.IdContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)


    class RelExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLanguageParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicLanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicLanguageParser.ExpressionContext,i)

        def GTE(self):
            return self.getToken(BasicLanguageParser.GTE, 0)
        def GT(self):
            return self.getToken(BasicLanguageParser.GT, 0)
        def LTE(self):
            return self.getToken(BasicLanguageParser.LTE, 0)
        def LT(self):
            return self.getToken(BasicLanguageParser.LT, 0)
        def EQ(self):
            return self.getToken(BasicLanguageParser.EQ, 0)
        def NEQ(self):
            return self.getToken(BasicLanguageParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelExpr" ):
                listener.enterRelExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelExpr" ):
                listener.exitRelExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelExpr" ):
                return visitor.visitRelExpr(self)
            else:
                return visitor.visitChildren(self)


    class ExpExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicLanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicLanguageParser.ExpressionContext,i)

        def EXP(self):
            return self.getToken(BasicLanguageParser.EXP, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpExpr" ):
                listener.enterExpExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpExpr" ):
                listener.exitExpExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpExpr" ):
                return visitor.visitExpExpr(self)
            else:
                return visitor.visitChildren(self)


    class FuncExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def func(self):
            return self.getTypedRuleContext(BasicLanguageParser.FuncContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncExpr" ):
                listener.enterFuncExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncExpr" ):
                listener.exitFuncExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncExpr" ):
                return visitor.visitFuncExpr(self)
            else:
                return visitor.visitChildren(self)


    class OrExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicLanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicLanguageParser.ExpressionContext,i)

        def OR(self):
            return self.getToken(BasicLanguageParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrExpr" ):
                return visitor.visitOrExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulDivExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLanguageParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicLanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicLanguageParser.ExpressionContext,i)

        def MUL(self):
            return self.getToken(BasicLanguageParser.MUL, 0)
        def DIV(self):
            return self.getToken(BasicLanguageParser.DIV, 0)
        def IDIV(self):
            return self.getToken(BasicLanguageParser.IDIV, 0)
        def MOD(self):
            return self.getToken(BasicLanguageParser.MOD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivExpr" ):
                listener.enterMulDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivExpr" ):
                listener.exitMulDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivExpr" ):
                return visitor.visitMulDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class ArrExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicLanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicLanguageParser.ExpressionContext,i)

        def LPARENSQ(self):
            return self.getToken(BasicLanguageParser.LPARENSQ, 0)
        def RPARENSQ(self):
            return self.getToken(BasicLanguageParser.RPARENSQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrExpr" ):
                listener.enterArrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrExpr" ):
                listener.exitArrExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrExpr" ):
                return visitor.visitArrExpr(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(BasicLanguageParser.SUB, 0)
        def expression(self):
            return self.getTypedRuleContext(BasicLanguageParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinusExpr" ):
                listener.enterUnaryMinusExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinusExpr" ):
                listener.exitUnaryMinusExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinusExpr" ):
                return visitor.visitUnaryMinusExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumberExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def number(self):
            return self.getTypedRuleContext(BasicLanguageParser.NumberContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class NotExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(BasicLanguageParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(BasicLanguageParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpr" ):
                listener.enterNotExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpr" ):
                listener.exitNotExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpr" ):
                return visitor.visitNotExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLanguageParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(BasicLanguageParser.LPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(BasicLanguageParser.ExpressionContext,0)

        def RPAREN(self):
            return self.getToken(BasicLanguageParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddSubExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BasicLanguageParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicLanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicLanguageParser.ExpressionContext,i)

        def ADD(self):
            return self.getToken(BasicLanguageParser.ADD, 0)
        def SUB(self):
            return self.getToken(BasicLanguageParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubExpr" ):
                listener.enterAddSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubExpr" ):
                listener.exitAddSubExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubExpr" ):
                return visitor.visitAddSubExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BasicLanguageParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                localctx = BasicLanguageParser.UnaryMinusExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 288
                self.match(BasicLanguageParser.SUB)
                self.state = 289
                self.expression(15)
                pass
            elif token in [51]:
                localctx = BasicLanguageParser.StringExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 290
                self.string()
                pass
            elif token in [49]:
                localctx = BasicLanguageParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 291
                self.number()
                pass
            elif token in [50]:
                localctx = BasicLanguageParser.FloatExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 292
                self.float_()
                pass
            elif token in [22, 23, 24, 25]:
                localctx = BasicLanguageParser.FuncExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 293
                self.func()
                pass
            elif token in [48]:
                localctx = BasicLanguageParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 294
                self.id_()
                pass
            elif token in [18]:
                localctx = BasicLanguageParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 295
                self.match(BasicLanguageParser.LPAREN)
                self.state = 296
                self.expression(0)
                self.state = 297
                self.match(BasicLanguageParser.RPAREN)
                pass
            elif token in [16]:
                localctx = BasicLanguageParser.NotExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 299
                self.match(BasicLanguageParser.NOT)
                self.state = 300
                self.expression(4)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 328
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 326
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                    if la_ == 1:
                        localctx = BasicLanguageParser.MulDivExprContext(self, BasicLanguageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 303
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 304
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 142) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 305
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = BasicLanguageParser.AddSubExprContext(self, BasicLanguageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 306
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 307
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==4 or _la==5):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 308
                        self.expression(7)
                        pass

                    elif la_ == 3:
                        localctx = BasicLanguageParser.RelExprContext(self, BasicLanguageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 309
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 310
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16128) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 311
                        self.expression(6)
                        pass

                    elif la_ == 4:
                        localctx = BasicLanguageParser.AndExprContext(self, BasicLanguageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 312
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 313
                        self.match(BasicLanguageParser.AND)
                        self.state = 314
                        self.expression(4)
                        pass

                    elif la_ == 5:
                        localctx = BasicLanguageParser.OrExprContext(self, BasicLanguageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 315
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 316
                        self.match(BasicLanguageParser.OR)
                        self.state = 317
                        self.expression(3)
                        pass

                    elif la_ == 6:
                        localctx = BasicLanguageParser.ExpExprContext(self, BasicLanguageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 318
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 319
                        self.match(BasicLanguageParser.EXP)
                        self.state = 320
                        self.expression(1)
                        pass

                    elif la_ == 7:
                        localctx = BasicLanguageParser.ArrExprContext(self, BasicLanguageParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 321
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 322
                        self.match(BasicLanguageParser.LPARENSQ)
                        self.state = 323
                        self.expression(0)
                        self.state = 324
                        self.match(BasicLanguageParser.RPARENSQ)
                        pass

             
                self.state = 330
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
            return self.getTypedRuleContext(BasicLanguageParser.LenfuncContext,0)


        def valfunc(self):
            return self.getTypedRuleContext(BasicLanguageParser.ValfuncContext,0)


        def isnanfunc(self):
            return self.getTypedRuleContext(BasicLanguageParser.IsnanfuncContext,0)


        def randfunc(self):
            return self.getTypedRuleContext(BasicLanguageParser.RandfuncContext,0)


        def getRuleIndex(self):
            return BasicLanguageParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = BasicLanguageParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_func)
        try:
            self.state = 335
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.lenfunc()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
                self.valfunc()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 3)
                self.state = 333
                self.isnanfunc()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 4)
                self.state = 334
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
            return self.getToken(BasicLanguageParser.STRINGLITERAL, 0)

        def getRuleIndex(self):
            return BasicLanguageParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = BasicLanguageParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(BasicLanguageParser.STRINGLITERAL)
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
            return self.getToken(BasicLanguageParser.NUMBER, 0)

        def getRuleIndex(self):
            return BasicLanguageParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)




    def number(self):

        localctx = BasicLanguageParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(BasicLanguageParser.NUMBER)
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
            return self.getToken(BasicLanguageParser.FLOAT, 0)

        def getRuleIndex(self):
            return BasicLanguageParser.RULE_float

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat" ):
                return visitor.visitFloat(self)
            else:
                return visitor.visitChildren(self)




    def float_(self):

        localctx = BasicLanguageParser.FloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(BasicLanguageParser.FLOAT)
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
            return self.getToken(BasicLanguageParser.ID, 0)

        def getRuleIndex(self):
            return BasicLanguageParser.RULE_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)




    def id_(self):

        localctx = BasicLanguageParser.IdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_id)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.match(BasicLanguageParser.ID)
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
            return self.getToken(BasicLanguageParser.LEN, 0)

        def LPAREN(self):
            return self.getToken(BasicLanguageParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(BasicLanguageParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(BasicLanguageParser.RPAREN, 0)

        def getRuleIndex(self):
            return BasicLanguageParser.RULE_lenfunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLenfunc" ):
                listener.enterLenfunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLenfunc" ):
                listener.exitLenfunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLenfunc" ):
                return visitor.visitLenfunc(self)
            else:
                return visitor.visitChildren(self)




    def lenfunc(self):

        localctx = BasicLanguageParser.LenfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_lenfunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(BasicLanguageParser.LEN)
            self.state = 346
            self.match(BasicLanguageParser.LPAREN)
            self.state = 347
            self.expression(0)
            self.state = 348
            self.match(BasicLanguageParser.RPAREN)
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
            return self.getToken(BasicLanguageParser.VAL, 0)

        def LPAREN(self):
            return self.getToken(BasicLanguageParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(BasicLanguageParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(BasicLanguageParser.RPAREN, 0)

        def getRuleIndex(self):
            return BasicLanguageParser.RULE_valfunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValfunc" ):
                listener.enterValfunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValfunc" ):
                listener.exitValfunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValfunc" ):
                return visitor.visitValfunc(self)
            else:
                return visitor.visitChildren(self)




    def valfunc(self):

        localctx = BasicLanguageParser.ValfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_valfunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(BasicLanguageParser.VAL)
            self.state = 351
            self.match(BasicLanguageParser.LPAREN)
            self.state = 352
            self.expression(0)
            self.state = 353
            self.match(BasicLanguageParser.RPAREN)
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
            return self.getToken(BasicLanguageParser.ISNAN, 0)

        def LPAREN(self):
            return self.getToken(BasicLanguageParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(BasicLanguageParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(BasicLanguageParser.RPAREN, 0)

        def getRuleIndex(self):
            return BasicLanguageParser.RULE_isnanfunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIsnanfunc" ):
                listener.enterIsnanfunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIsnanfunc" ):
                listener.exitIsnanfunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIsnanfunc" ):
                return visitor.visitIsnanfunc(self)
            else:
                return visitor.visitChildren(self)




    def isnanfunc(self):

        localctx = BasicLanguageParser.IsnanfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_isnanfunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(BasicLanguageParser.ISNAN)
            self.state = 356
            self.match(BasicLanguageParser.LPAREN)
            self.state = 357
            self.expression(0)
            self.state = 358
            self.match(BasicLanguageParser.RPAREN)
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
            return self.getToken(BasicLanguageParser.RAND, 0)

        def LPAREN(self):
            return self.getToken(BasicLanguageParser.LPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BasicLanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BasicLanguageParser.ExpressionContext,i)


        def COMMA(self):
            return self.getToken(BasicLanguageParser.COMMA, 0)

        def RPAREN(self):
            return self.getToken(BasicLanguageParser.RPAREN, 0)

        def getRuleIndex(self):
            return BasicLanguageParser.RULE_randfunc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRandfunc" ):
                listener.enterRandfunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRandfunc" ):
                listener.exitRandfunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRandfunc" ):
                return visitor.visitRandfunc(self)
            else:
                return visitor.visitChildren(self)




    def randfunc(self):

        localctx = BasicLanguageParser.RandfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_randfunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(BasicLanguageParser.RAND)
            self.state = 361
            self.match(BasicLanguageParser.LPAREN)
            self.state = 362
            self.expression(0)
            self.state = 363
            self.match(BasicLanguageParser.COMMA)
            self.state = 364
            self.expression(0)
            self.state = 365
            self.match(BasicLanguageParser.RPAREN)
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
        self._predicates[23] = self.expression_sempred
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
         




