"""
Problem: Find First and Last Position of Element in Sorted Array
Platform: LeetCode
Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Difficulty: Medium

Pattern:
- Binary Search

Approach:
Use binary search twice:
- First, find the first occurrence of the target.
- Then, find the last occurrence of the target.
Return both indices. If the target is not found, return [-1, -1].

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def search_range(nums,target): 
    def lower_bound(nums,target):
        n=len(nums)
        low=0
        high=n-1
        lb=len(nums)
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]>=target:
                lb=mid
                high=mid-1
            else:
                low=mid+1
        return lb

    def upper_bound(nums,target):
        n=len(nums)
        low=0
        high=n-1
        lub=len(nums)
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]>target:
                ub=mid
                high=mid-1
            else:
                low=mid+1
        return ub

    lb=lower_bound(nums,target)
    if lb==len(nums) or nums[lb]!=target:
        return[-1,-1]
    ub=upper_bound(nums,target)
    return [lb,ub-1]

#Test case
nums = [5,7,7,8,8,10]
target = 6
print(search_range(nums,target))

