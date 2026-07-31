"""
Problem: Single Number
Platform: LeetCode
Link: https://leetcode.com/problems/single-number/
Difficulty: Easy

Pattern:
- Bit Manipulation
- XOR

Approach:
Initialize an answer variable as 0. Traverse the array and XOR
each element with the answer. Since x ^ x = 0 and 0 ^ x = x,
all duplicate numbers cancel out, leaving only the number that
appears once.

Time Complexity: O(n)
Space Complexity: O(1)
"""
def single(nums):
    ans=0
    for num in nums:
        ans^=num
    return ans

#Test case
nums = [4,1,2,1,2]
print(single(nums))
