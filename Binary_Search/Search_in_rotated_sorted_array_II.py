"""
Problem: Search in Rotated Sorted Array II
Platform: LeetCode
Link: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
Difficulty: Medium

Pattern:
- Binary Search

Approach:
Use binary search to identify the sorted half of the array.
If duplicate elements prevent determining the sorted half,
shrink the search space by moving both pointers inward.
Continue until the target is found or the search space becomes empty.

Time Complexity: O(log n) on average, O(n) in the worst case
Space Complexity: O(1)
"""
def search(nums,target):
    n=len(nums)
    low=0
    high=n-1
    while low<=high:
        mid=low+(high-low)//2
        if nums[mid]==target:
            return True
        elif nums[low]==nums[mid]==nums[high]:
            low+=1
            high-=1
            continue 
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
    return False

#Test Case
nums=[7,7,7,7,7,1,2,3,4,5,7,7]
target=0
print(search(nums,target))
