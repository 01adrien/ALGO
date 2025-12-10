from collections import deque
from dataclasses import dataclass

@dataclass
class ParserResult:
    num: int
    tokens: deque[str]

def token(src: str, index: int) -> tuple[int , str]:
    i = 0
    while (index + i < len(src) and src[index + i] != " "):
        i += 1
    tok = src[index: index + i]
    
    return (index + i, tok)


def skip_white(src: str, index: int) -> int:
    while (index < len(src) and src[index] == " "):
        index += 1
        
    return index


def tokenize(src: str) -> list[str]:
    index = 0
    tokens = []
    while (index < len(src)):
        (i, t) = token(src, index)
        tokens.append(t)
        index = skip_white(src, i)
        
    return tokens


def parse_expr(tokens: deque) -> ParserResult:
    a = int(tokens.popleft())
    while len(tokens) and tokens[0] in ['+', '-']:
        op = tokens.popleft()
        b = int(tokens.popleft())
        a += b if op == '+' else -b

    return ParserResult(a, tokens)


def eval(src):
    tokens = deque(tokenize(src))
    res = parse_expr(tokens)
    print(res.num)

eval("1 - 2 + 3 - 4 + 5")


'''
expr := term ( + | - ) term

term := factor ( * | / ) factor

factor := [0-9]+

'''