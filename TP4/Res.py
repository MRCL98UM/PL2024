import ply.lex as lex
import sys

tokens = (
    'SELECT',
    'FROM',
    'WHERE',
    'WORD',
    'COMMA',
    'LESSER',
    'GREATER',
    'EQUALS',
    'NUMBER',
    'GREATEREQUAL',
    'LESSEREQUAL',
)

t_SELECT = r'SELECT'
t_FROM = r'FROM'
t_WHERE = r'WHERE'

t_COMMA = r','
t_LESSER = r'<'
t_GREATER = r'>'
t_EQUALS = r'='
t_GREATEREQUAL = r'>='
t_LESSEREQUAL = r'<='
t_WORD = r'[a-zA-Z_][a-zA-Z0-9_]*'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def main():
    lexer = lex.lex()
    for line in sys.stdin:
        lexer.input(line)
        for tok in lexer:
            print(tok)
            print(tok.type, tok.value, tok.lineno, tok.lexpos)


if __name__ == "__main__":
    main()
