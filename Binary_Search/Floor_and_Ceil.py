"""
Problem: Floor and Ceil in Sorted Array
Platform: DSA Concept

Difficulty: Easy

Pattern:
- Binary Search

Approach:
Use binary search to find the floor and ceil of the target.
The floor is the greatest element less than or equal to the target,
and the ceil is the smallest element greater than or equal to the target.

Time Complexity: O(log n)
Space Complexity: O(1)
"""


def floor_and_ceil(nums,target):
    n=len(nums)
    low=0
    high=n-1
    floor=-1
    ceil=-1
    while low<=high:
        mid=low+(high-low)//2
        if nums[mid]==target:
            return [nums[mid],nums[mid]]
        elif nums[mid]<target:
            floor=nums[mid]
            low=mid+1
        else:
            ceil=nums[mid]
            high=mid-1
    return [floor,ceil]

#Test Case
nums = [2,4,6,8,10]
target=7
print(floor_and_ceil(nums,target))