"""
Problem: Missing Number
Platform: LeetCode
Link: https://leetcode.com/problems/missing-number/
Difficulty: Easy

Pattern:
- Array
- Math (Summation Formula)

Approach:
1. Calculate the expected sum of numbers from 0 to n.
2. Calculate the actual sum of the given array.
3. Return the difference.

Time Complexity: O(n)
Space Complexity: O(1)
"""



def missingNumber( nums):
    n = len(nums)

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum

#Test Case
nums=[0,3,1]
print(missingNumber(nums))
