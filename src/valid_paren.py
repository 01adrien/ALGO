'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

'''


from functools import reduce


def valid_paren(src: str) -> bool:
    matcher = {'(': ')', '[': ']', '{': '}'}
    stack = []

    for char in src:
        if char in matcher:  
            stack.append(char)
        elif char in matcher.values(): 
            if not stack or matcher[stack.pop()] != char:
                return False
    return len(stack) == 0



def valid_paren_fp(src: str) -> bool:
    matcher = {'(': ')', '[': ']', '{': '}'}

    def reducer(stack, char):
        if char in matcher:
            return stack + [char]
        elif char in matcher.values():  
            if not stack or matcher[stack[-1]] != char:
                return None  
            return stack[:-1]
        return stack  

    result = reduce(lambda acc, c: reducer(acc, c) if acc is not None else None, src, [])
    return result is not None and len(result) == 0


def test_valid_paren():
    assert valid_paren("()") == True
    assert valid_paren("()[]{}") == True
    assert valid_paren("{[()]}") == True
    assert valid_paren("") == True  # chaîne vide
    assert valid_paren("(([]){})") == True

    assert valid_paren("(") == False
    assert valid_paren(")") == False
    assert valid_paren("(]") == False
    assert valid_paren("([)]") == False
    assert valid_paren("{[}") == False
    assert valid_paren("((())") == False
    assert valid_paren("())") == False

    assert valid_paren("([]{})[]{}()") == True
    assert valid_paren("([{}({})])") == True
    assert valid_paren("([{}({})])(") == False

    print("all tests pass !")


test_valid_paren()
