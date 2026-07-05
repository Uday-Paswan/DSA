"""
Problem: Binary Search
Platform: LeetCode
Link: https://leetcode.com/problems/binary-search/
Difficulty: Easy

Pattern:
- Binary Search

Approach:
Maintain two pointers, low and high, representing the search range.
Find the middle element and compare it with the target.
If the target is smaller, search the left half; otherwise, search the right half.
Repeat until the target is found or the search space becomes empty.

Time Complexity: O(log n)
Space Complexity: O(1)
"""
def binary_search(nums,target):
    n=len(nums)
    low=0
    high=n-1
    while low<=high:
        mid=low+(high-low)//2 #(low+high)//2
        if nums[mid]==target:
            return mid 
        elif nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

#Test Case
nums = [-1,0,3,5,9,12]
target = 2
print(binary_search(nums,target))