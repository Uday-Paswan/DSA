"""
Problem: Maximum Subarray
Platform: LeetCode
Link: https://leetcode.com/problems/maximum-subarray/
Difficulty: Medium

Pattern:
- Array
- Dynamic Programming (Kadane's Algorithm)

Approach:
Maintain a running sum of the current subarray.
If the running sum becomes negative, reset it because
a negative sum cannot increase the sum of a future subarray.
Keep track of the maximum subarray sum seen so far.

Time Complexity: O(n)
Space Complexity: O(1)
"""


def maxSubArray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum=max(nums[i],current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum
    
#Test case
nums=[-2,1,-3,4,-1]
print(maxSubArray(nums))