"""
Problem: Count Occurrences in Sorted Array
Platform: DSA Concept

Difficulty: Easy

Pattern:
- Binary Search

Approach:
Find the lower bound and upper bound of the target.
The difference between the upper bound and lower bound
gives the total number of occurrences.

Time Complexity: O(log n)
Space Complexity: O(1)
"""
def count_occurrence(nums,target): 
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
        ub=len(nums)
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]>target:
                ub=mid
                high=mid-1
            else:
                low=mid+1
        return ub

    lb=lower_bound(nums,target)
    ub=upper_bound(nums,target)
    return ub-lb

#Test Case
nums = [1,2,2,2,3,4,5]
target = 2
print(count_occurrence(nums,target))
