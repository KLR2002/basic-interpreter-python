grammar BasicExpression;
import BasicLexer;

prog: stat+;

stat
    : expression NEWLINE
    | NEWLINE
    ;

expression
	: SUB expression							# unaryMinusExpr
    | string                                    # StringExpr
    | number                                    # NumberExpr
    | float                                     # FloatExpr
    | func                                      # FuncExpr
    | id                                        # IdExpr
    | (LPAREN expression RPAREN)                # ParenExpr
	| expression LPARENSQ expression RPARENSQ	# ArrExpr
    | expression op=(MUL|DIV|IDIV|MOD) expression    # MulDivExpr
    | expression op=(ADD|SUB) expression        # AddSubExpr
    | expression op=(GTE|GT|LTE|LT|EQ|NEQ) expression   # RelExpr
    | NOT expression                            # NotExpr
    | expression AND expression                 # AndExpr
    | expression OR expression                  # OrExpr
    | <assoc=right> expression EXP expression   # ExpExpr
    ;

func
    : lenfunc
    | valfunc
    | isnanfunc
    | randfunc
    ;

string
    : STRINGLITERAL
    ;

number
    : NUMBER
    ;

float
    : FLOAT
    ;

id
    : ID
    ;

lenfunc
    : LEN LPAREN expression RPAREN
    ;

valfunc
    : VAL LPAREN expression RPAREN
    ;

isnanfunc
    : ISNAN LPAREN expression RPAREN
    ;

randfunc
    : RAND LPAREN expression COMMA expression RPAREN
    ;

