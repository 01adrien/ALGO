from typing import List

'''
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 

'''


def contain_duplicate(nums):
    if len(nums) <= 1:
        return False

    mid = len(nums) // 2

    if contain_duplicate(nums[:mid]) or contain_duplicate(nums[mid:]):
        return True

    left_set = set(nums[:mid])
    right_set = set(nums[mid:])
    if left_set & right_set:
        return True

    return False


print(contain_duplicate([1,1,2,3]))