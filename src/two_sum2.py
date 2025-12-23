'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

 

Constraints:

    2 <= numbers.length <= 3 * 104
    -1000 <= numbers[i] <= 1000
    numbers is sorted in non-decreasing order.
    -1000 <= target <= 1000
    The tests are generated such that there is exactly one solution.



'''

import bisect
from typing import List
from binary_search import binary_search 
from TestFramework import TestFramework


def two_sum_naive(nums : List[int], target : int) -> List[int]:

    res = []    

    for i in range(len(nums)):
        for j in range(i + 1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i + 1, j + 1]
            j += 1
        i += 1
    
    return res


def two_sum_log(nums : List[int], target : int) -> List[int]:
    res = []
    
    for i in range(len(nums)):
        needed = target - nums[i]
        j = bisect.bisect_left(nums, needed, i + 1)
        if j < len(nums) and nums[j] == needed:
            return [i + 1, j + 1]
    
    return res

def two_sum_opti(nums : List[int], target : int) -> List[int]:
    res = []
    
    return res


test_cases = [
    (([1, 2], 3), [1, 2]),
    (([2, 7, 11, 15], 9), [1, 2]),
    (([-3, -1, 0, 2, 4], 1), [1, 5]),
    (([1, 2, 3, 4, 4, 9], 8), [4, 5]),
    (([1, 1, 3, 5, 7], 2), [1, 2]),
    (([1, 2, 3, 4, 6, 8], 14), [5, 6]),
    (([0, 0, 3, 4], 0), [1, 2]),
    (([-10, -8, -3, -1], -11), [1, 4]),
    (([1, 2, 4, 6, 10, 20, 40], 26), [4, 6]),
    (([9, 2, 2, 3, 5], 4), [2, 3]),
    (([1, 2, 2, 3, 4], 4), [1, 4]),
    (([1, 2, 3, 4, 5, 6, 7], 7), [1, 6]),
]



def worst_cases(n=1000):
    numbers = list(range(n))
    target = numbers[-2] + numbers[-1]
    return [(numbers, target)]


def best_cases(n=1000):
    numbers = list(range(n))
    target = numbers[0] + numbers[1]
    return [(numbers, target)]


def sparse_cases(n=1000):
    numbers = [i * 10 for i in range(n)]
    target = numbers[n // 3] + numbers[n // 2]
    return [(numbers, target)]


fns = [
    two_sum_naive,
    two_sum_log
]

tf = TestFramework()

# tf.add_test(two_sum_naive, test_cases)
tf.add_test(two_sum_log, test_cases)

tf.add_case_type("worst", worst_cases)
tf.add_case_type("best", best_cases)
tf.add_case_type("sparse", sparse_cases)

tf.run_tests()
# tf.run_benchmarks(fns)