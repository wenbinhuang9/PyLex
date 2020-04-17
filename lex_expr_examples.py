

from lexer import Lexer

tokenDefinition = {'NUMBER' : r'[0-9]+', "OPERATOR": r'\+|\-', "IGNORE" : r'\s'}

lex = Lexer(tokenDefinition)

input = "23 + 31 - 13"
lex.run(input)

while lex.hasNext():
    tok = lex.nextToken()
    print (tok)

