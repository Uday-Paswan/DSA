"""
Concept: Upper Bound

Difficulty: Easy

Pattern:
- Binary Search

Approach:
Use binary search to find the first index where the element
is strictly greater than the target.
If no such element exists, return the size of the array.

Time Complexity: O(log n)
Space Complexity: O(1)
"""


def upper_bound(nums,target):
    n=len(nums)
    low=0
    high=n-1
    ub=n
    while low<=high:
        mid=low+(high-low)//2
        if nums[mid]>target:
            ub=mid
            high=mid-1
        else:
            low=mid+1
    return ub

#Test Case 
nums=[1,1,1,2,2,3,4,5,6,6]
target=4
print(upper_bound(nums,target))