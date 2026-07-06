"""
Concept: Lower Bound

Difficulty: Easy

Pattern:
- Binary Search

Approach:
Use binary search to find the first index where the element
is greater than or equal to the target.
If no such element exists, return the size of the array.

Time Complexity: O(log n)
Space Complexity: O(1)
"""


def lower_bound(nums,target):
    n=len(nums)
    low=0
    high=n-1
    lb=n
    while low<=high:
        mid=low+(high-low)//2
        if nums[mid]>=target:
            lb=mid
            high=mid-1
        else:
            low=mid+1
    return lb

#Test case
nums=[1,1,1,2,3,4,5,6,7,8,8,9]
target=10
print(lower_bound(nums,target))
