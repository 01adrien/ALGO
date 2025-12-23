'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101


 

Constraints:

    0 <= n <= 105

 

Follow up:

    It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
    Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?


'''

from typing import List
from TestFramework import TestFramework


def get_set_bits(n : int) -> int:
    return n if n == 0 or n == 1 else (n & 1) + get_set_bits(n >> 1)

def counting_bits_naive(n : int) -> List[int]:
    res = []
    for i in range(0, n + 1):
        res.append(get_set_bits(i))
    
    return res



def counting_bits_opti(n : int) -> List[int]:

    res = []

    
    return res

    



test_cases = [
    (0, [0]),
    (1, [0, 1]),
    (2, [0, 1, 1]),
    (3, [0, 1, 1, 2]),
    (4, [0, 1, 1, 2, 1]),                       
    (5, [0, 1, 1, 2, 1, 2]),                    
    (6, [0, 1, 1, 2, 1, 2, 2]),                 
    (7, [0, 1, 1, 2, 1, 2, 2, 3]),              
    (8, [0, 1, 1, 2, 1, 2, 2, 3, 1]),           
    (9, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2]),        
    (10,[0,1,1,2,1,2,2,3,1,2,2]),               
    (15,[0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4]),     
    (16,[0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1]),   
    (31,[0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4,1,2,2,3,2,3,3,4,2,3,3,4,3,4,4,5]),
]



tf = TestFramework()

# tf.add_test(counting_bits_naive, test_cases)
tf.add_test(counting_bits_opti, test_cases)

tf.run_tests()


def worst_cases():
    pass

def best_cases():
    pass

def sparse_cases():
    pass



cases = {
    "worst": worst_cases(),
    "best": best_cases(),
    "sparse": sparse_cases(),
}

fns = [

]

for name, values in cases.items():
    print(f"\n=== {name.upper()} CASES ===")
    for fn in fns:
        t = tf.benchmark(fn, values)
        print(f"{fn.__name__:25s} {t:.6f}s")
