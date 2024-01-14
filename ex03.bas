REM GCD and LCM

INPUT "a =" a
INPUT "b =" b

a = VAL(a)
b = VAL(b)
d = a*b

WHILE b <> 0
    c = a
    a = b
    b = c MOD b
END

PRINT "GCD(a,b) = " + a
PRINT "LCM(a,b) = " + d DIV a