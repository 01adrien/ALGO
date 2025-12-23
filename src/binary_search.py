from typing import List


def binary_search(nums: List[int], n: int, start: int = 0, end: int = None) -> int:
    if end is None:
        end = len(nums)
        
    if start >= end:
        return -1
    
    mid = (start + end) // 2
    
    if nums[mid] == n:
        return mid
    
    elif nums[mid] > n:
        return binary_search(nums, n, start, mid)
    
    else:
        return binary_search(nums, n, mid + 1, end)