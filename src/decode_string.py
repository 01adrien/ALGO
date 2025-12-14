'''

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets 
is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; 
there are no extra white spaces, square brackets are well-formed, etc. 
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.


Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef" 

'''

def decode_string(src: str) -> str:

    def fn(s: str, i: int = 0, acc: str = "", num: int = 0) -> tuple[str, int]:
        
        if i >= len(s):
            return acc, i

        c = s[i]

        if c.isdigit():
            new_num = num * 10 + int(c)
            return fn(s, i + 1, acc, new_num)

        elif c == '[':
            sub_str, consumed = fn(s, i + 1)
            acc += sub_str * num
            return fn(s, consumed + 1, acc, 0)

        elif c == ']':
            return acc, i

        else:
            return fn(s, i + 1, acc + c, num)

    decoded, _ = fn(src)
    
    return decoded

        
    

print(decode_string("3[a2[c]]"))

        
def test():    
    tests_complex = [
        ("3[a]", "aaa"),
        ("2[ab]", "abab"),

        ("3[a]2[b]", "aaabb"),
        ("4[x]1[y]3[z]", "xxxxyzzz"),

        ("3[a2[c]]", "accaccacc"),
        ("2[abc3[de]]", "abcdededeabcdedede"),

        ("2[3[a]b]", "aaabaaab"),
        ("3[a2[b4[F]c]]", "abFFFFcbFFFFcabFFFFcbFFFFcabFFFFcbFFFFcabFFFFcbFFFFc"),

        ("a2[b3[c]]d", "abcccbcccd"), 
        
        ("10[a2[b]]", "abbabbabbabbabbabbabbabbabbabb"),
    ]

    for s, expected in tests_complex:
        result = decode_string(s)
        print(f"Input: {s} -> Output: {result} | Expected: {expected} | {'PASS' if result == expected else 'FAIL'}")


