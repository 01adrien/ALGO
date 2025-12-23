'''

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

 

Constraints:

    n == nums.length
    1 <= n <= 5 * 104
    -109 <= nums[i] <= 109
    The input is generated such that a majority element will exist in the array.

 
Follow-up: Could you solve the problem in linear time and in O(1) space?

'''

def majority(nums: list[int]) -> int:
    
    '''
    Complexité temporelle : O(n log n)
    Complexité spatiale : O(log n) (pile de récursion)
    '''
    if len(nums) == 1:
        return nums[0]

    mid = len(nums) // 2
    
    left = majority(nums[:mid])
    right = majority(nums[mid:])
    
    if left == right:
        return left
    
    count_l = nums.count(left)
    count_r = nums.count(right)

    return left if count_l > count_r else right




def majority_boyer_moore(nums: list[int]) -> int:
    
    '''
    Complexité temporelle : O(n)
    Complexité spatiale : O(1) (2 variable)
    '''
    
    candidat = nums[0]
    i = 1
    
    for n in nums[1:]:
        if n != candidat:
            i -= 1
        else:
            i += 1
        if i == 0:
            candidat = n
            i = 1
        
    return candidat


print(majority_boyer_moore([7] * 30000 + [1] * 20000))