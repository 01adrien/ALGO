'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

Example 3:

Input: nums = [1]

Output: 1

 

Constraints:

    1 <= nums.length <= 3 * 104
    -3 * 104 <= nums[i] <= 3 * 104
    Each element in the array appears twice except for one element which appears only once.

'''

from collections import defaultdict



def single_number(l: list[int]) -> int :
    
    acc = defaultdict(int)
    for n in l:
        acc[n] += 1
        if acc[n] == 2:
            acc.pop(n, None)
    
    [key] = acc
    
    return key



def single_number_rec(l : list[int], acc: int = 0) -> int:
    
        return acc if not l else single_number_rec(l[1:], acc ^ l[0])




print(single_number_rec([4,1,2,1,2]))
