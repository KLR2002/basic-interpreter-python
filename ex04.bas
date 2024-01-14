REM simple primality test, for loop with step, if/else if/else

INPUT "n =" n
n = VAL(n)

IF n <= 1 THEN
    PRINT n + " is not a prime number"
ELSE IF n = 2 OR n = 3 THEN
    PRINT n + " is a prime number"
ELSE IF n MOD 2 = 0 OR n MOD 3 = 0 THEN
    PRINT n + " is not a prime number"
ELSE
    flag = 1
    FOR i = 5 TO n DIV 2 STEP 6
        IF n MOD i = 0 OR n MOD (i + 2) = 0 THEN
            PRINT n + " is not a prime number"
            flag = 0
            EXIT
        END
    NEXT

    IF flag THEN
        PRINT n + " is a prime number"
    END
END