'''
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:

Input: n = 3
Output: false

 

Constraints:

    -231 <= n <= 231 - 1

 
Follow up: Could you solve it without loops/recursion?
 
     1
    10
   100 
  1000
'''

import sys


def power_rec_naive(n : int, exp : int = 0) -> bool:
    if 2 ** exp > n or n < 0:
        return False
    if 2 ** exp == n:
        return True
    return power_rec_naive(n, exp + 1)


def power_rec(n : int, acc : int = 1) -> bool:
    if acc > n or n < 0:
        return False
    if  acc == n :
        return True
    return power_rec(n, acc * 2)


def power_bin(n : int) -> bool:
    return n > 0 and (n & (n - 1)) == 0

def test(fn):
    test_cases = [
        (1, True),    
        (2, True),    
        (3, False),   
        (4, True),    
        (5, False),   
        (8, True),    
        (16, True),   
        (31, False),  
        (32, True),   
        (64, True),   
        (127, False), 
        (128, True),  
        (0, False),   
        (-2, False),  
        (-8, False),  
        (1024, True), 
        (1023, False) 
    ]
    
    for n, expected in test_cases:
        result = fn(n)
        print(f"fn({n}) = {result}, attendu: {expected}, {'✓' if result == expected else '✗'}")



test(power_rec)
# print(bin(4 & 3))
# print(bin(4 << 1))    