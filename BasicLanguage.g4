grammar BasicLanguage;

import BasicLexer, BasicExpression;

prog: block EOF;

statement
    : letStmt
	| arrStmt
	| arrElementStmt
    | printStmt
    | inputStmt
    | ifStmt
    | subStmt
    | forStmt
    | whileStmt
    | repeatStmt
    | continueStmt
    | exitStmt
    | swapFunc
    | COMMENT;
	
block
    : (statement (NEWLINE+ | EOF))*
    ;

letStmt
	: LET? vardecl EQ expression
	;

arrStmt
	: DIM vardecl expression
	;

arrElementStmt
    : INDEX varname LPARENSQ expression RPARENSQ EQ expression
	;

vardecl
	: varname varsuffix?
	;

varname
	: ID
	;

varsuffix
	: DOLLAR
	;

printStmt
	: PRINT expression;

inputStmt
	: INPUT string vardecl
	;

ifStmt
	: IF expression NEWLINE* THEN NEWLINE+ block elifStmt* elseStmt? END
	;

elifStmt
    : ELSE IF expression NEWLINE* THEN NEWLINE+ block
    ;

elseStmt
    : ELSE NEWLINE+ block
    ;

subStmt
    : SUBROUTINE ID LPAREN (ID (COMMA ID)* )* RPAREN NEWLINE+ block END
    ;

subCall
    : ID LPAREN (expression (COMMA expression)* )* RPAREN
    ;

forStmt
	: FOR vardecl EQ expression TO expression (STEP expression)? NEWLINE+ block NEXT
	;

whileStmt
	: WHILE expression NEWLINE+ block END
	;

repeatStmt
	: REPEAT NEWLINE+ block NEWLINE* UNTIL expression
	;

continueStmt
	: CONTINUE
	;

exitStmt
	: EXIT
	;

swapFunc
    : SWAP LPAREN expression COMMA expression RPAREN
    ;