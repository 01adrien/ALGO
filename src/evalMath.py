from collections import deque
from dataclasses import dataclass


@dataclass
class ParserResult:
    num: int
    tokens: deque[str]
    

def token(src: str, index: int) -> tuple[int , str]:
    i = 0
    
    if index + i < len(src) and src[index + i] == ')':
        return (index + i + 1, ')')
    
    while index + i < len(src) and src[index + i] not in [" ", "(", ")"]:
        i += 1
    
    if index + i < len(src) and src[index + i] == '(':
        return (index + i + 1, '(')
        
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


def parse_expr(tokens: deque[str]) -> ParserResult:
    res = parse_term(tokens)
    left, tokens = res.num, res.tokens
    while len(tokens) and tokens[0] in ['+', '-']:
        op = tokens.popleft()
        res2 = parse_term(tokens)
        right, tokens = res2.num, res2.tokens
        left += right if op == '+' else -right

    return ParserResult(left, tokens)


def parse_term(tokens: deque[str]) -> ParserResult:
    res = parse_factor(tokens)
    left, tokens = res.num, res.tokens
    while len(tokens) and tokens[0] in ['*', '/']:
        op = tokens.popleft()
        res2 = parse_factor(tokens)
        right, tokens = res2.num, res2.tokens
        left = left * right if op == '*' else left // right

    return ParserResult(left, tokens)
    


def parse_factor(tokens: deque[str]) -> ParserResult:
    tok = tokens.popleft()
    if tok.lstrip('-').isnumeric():
        return ParserResult(int(tok), tokens)
    elif tok == '(':
        res = parse_expr(tokens)
        if (len(res.tokens) == 0 or res.tokens.popleft() != ")"):
            raise Exception('mismatch paren')
        return res
    
    raise Exception("Unknow factor " + tok)


def eval(src):
    tokens = deque(tokenize(src))
    print(tokens)
    res = parse_expr(tokens)
    print(res.num)

eval("5 + -2")


'''
expr := term ( + | - ) term

term := factor ( * | / ) factor

factor := (-)?[0-9]+ | '(' expr ')'

'''