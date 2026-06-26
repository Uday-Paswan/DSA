"""
Problem: Max Consecutive Ones
Platform: LeetCode
Link: https://leetcode.com/problems/max-consecutive-ones/
Difficulty: Easy

Pattern:
- Array
- Traversal

Approach:
Traverse the array while maintaining a count of consecutive 1s.
Whenever a 0 is encountered, update the maximum count and reset
the current count.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def max_consecutive_ones(nums):
    count=0
    max_count=0
    for num in nums:
        if num==1:
            count+=1
        else:
            max_count=max(max_count,count)
            count=0
    return max(max_count,count)

#Test Case
nums=[1,1,0,1,1,1,1]
print(max_consecutive_ones(nums))