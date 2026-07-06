"""
Problem: Search Insert Position
Platform: LeetCode
Link: https://leetcode.com/problems/search-insert-position/
Difficulty: Easy

Pattern:
- Binary Search

Approach:
Use binary search to find the target in the sorted array.
If the target is not found, return the index where it should
be inserted to maintain the sorted order.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def insert_search(nums,target):
    n=len(nums)
    low=0
    high=n-1
    index=n
    while low<=high:
        mid=low+(high-low)//2
        if nums[mid]>=target:
            index=mid
            high=mid-1
        else:
            low=mid+1
    return index

#Test case
nums=[1,3,5,6]
target = 2
print(insert_search(nums,target))