"""
Problem: Find Minimum in Rotated Sorted Array
Platform: LeetCode
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Difficulty: Medium

Pattern:
- Binary Search

Approach:
Use binary search to determine which half of the array is sorted.
The minimum element always lies in the unsorted half or may be
the middle element itself. Narrow the search space until the
minimum element is found.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def minimum (nums):
    n=len(nums)
    low=0
    high=n-1
    mini=float("inf")
    while low<=high:
        mid=low+(high-low)//2
        if nums[low]<=nums[high]:
            mini=min(mini,nums[low])
            break
        if nums[low]<=nums[mid]:
            mini=min(mini,nums[low])
            low=mid+1
        else:
            mini=min(mini,nums[mid])
            high=mid-1
    return mini 

#Test Case
nums=[4,5,6,0,1,2,3]
print(minimum(nums))