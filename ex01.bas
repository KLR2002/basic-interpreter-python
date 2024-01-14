REM Bubble Sort
DIM arr 10
FOR i = 0 TO 9
    INDEX arr[i] = RAND(1, 100)
NEXT

PRINT "Before sorting: " + arr

FOR i=0 TO LEN(arr)-2
    FOR j=0 TO LEN(arr)-i-2
        IF arr[j] > arr[j+1] THEN
            SWAP(arr[j], arr[j+1])
        END
    NEXT
NEXT

PRINT "After sorting: " + arr

