"""
Problem: Search in Rotated Sorted Array
Platform: LeetCode
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
Difficulty: Medium

Pattern:
- Binary Search

Approach:
Use binary search to identify the sorted half of the array.
Check if the target lies within the sorted half and discard
the other half. Repeat until the target is found or the
search space becomes empty.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def search(nums,target):
    n=len(nums)
    low=0
    high=n-1
    while low<=high:
        mid=low+(high-low)//2
        if nums[mid]==target:
            return mid 
        elif nums[low]<=nums[mid]:
            if nums[low]<=target<nums[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if nums[mid]<target<=nums[mid]:
                low=mid+1
            else:
                high=mid-1
    return -1

#Test case
nums = [4,5,6,7,0,1,2]
target=3
print(search(nums,target))