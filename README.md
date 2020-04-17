# PyLex
A general lexical generator based on Python 

## How to use

```
from lexer import Lexer

# firstly, define your token type and corresponding regular expression

tokenDefinition = {'NUMBER' : r'[0-9]+', "OPERATOR": r'\+|\-', "IGNORE" : r'\s'}

lex = Lexer(tokenDefinition)

input = "23 + 31 - 13"
lex.run(input)

while lex.hasNext():
    tok = lex.nextToken()
    print (tok)
```

## TODO

1. support  lineno
2. support debugger



