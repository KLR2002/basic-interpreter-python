REM Input, Reverse String, Repeat

INPUT "Type sentence:" sentence

LET sentenceReversed = ""
LET j = LEN(sentence) - 1

REPEAT
    sentenceReversed = sentenceReversed + sentence[j]
    j = j - 1
UNTIL j < 0

PRINT sentenceReversed



