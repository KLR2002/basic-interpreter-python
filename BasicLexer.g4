lexer grammar BasicLexer;


//operatory arytmetyczne
MUL : '*' ;
DIV : '/' ;
IDIV : 'DIV' ;
ADD : '+' ;
SUB : '-' ;
EXP : '^' ;
MOD : 'MOD' ;


//operatory logiczne
NEQ : '<>' ;
GTE : '>=' ;
LTE : '<=' ;
GT  : '>' ;
LT  : '<' ;
EQ  : '=' ;

AND : 'AND' | 'and' ;
OR  : 'OR' | 'or' ;
NOT : 'NOT' | 'not' ;


//inne
COMMA  : ',' ;
LPAREN : '(' ;
RPAREN : ')' ;
LPARENSQ : '[' ;
RPARENSQ : ']' ;

//funkcje
LEN : 'LEN' | 'len' ;
VAL : 'VAL' | 'val' ;
ISNAN   : 'ISNAN' | 'isnan' ;
RAND    : 'RAND' | 'rand' ;
SWAP    : 'SWAP' | 'swap' ;


//słowa kluczowe
PRINT   : 'PRINT' | 'print' ;
INPUT   : 'INPUT' | 'input' ;
LET     : 'LET' | 'let' ;
DIM		: 'DIM' | 'dim' ;
INDEX   : 'INDEX' | 'index' ;
REM     : 'REM' | 'rem' ;
IF      : 'IF' | 'if' ;
THEN    : 'THEN' | 'then' ;
ELSE    : 'ELSE' | 'else' ;
END     : 'END' | 'end';
SUBROUTINE : 'SUB' | 'sub' ;
FOR     : 'FOR' | 'for' ;
WHILE   : 'WHILE' | 'while' ;
REPEAT  : 'REPEAT' | 'repeat' ;
UNTIL   : 'UNTIL' | 'until' ;
STEP    : 'STEP' | 'step' ;
NEXT    : 'NEXT' | 'next' ;
TO      : 'TO' | 'to' ;
CONTINUE    : 'CONTINUE' | 'continue' ;
EXIT    : 'EXIT' | 'exit' ;


//inne
COMMENT : REM ~[\r\n]* ;

//literały
ID              : [a-zA-Z]+ ;  
NUMBER          : [0-9]+ ;
FLOAT			: NUMBER '.' NUMBER? ;
STRINGLITERAL   : '"' ~ ["\r\n]* '"' ;
DOLLAR          : '$' ;
NEWLINE         :'\r'? '\n' ;  
WS              : [ \t]+ -> skip ; 



