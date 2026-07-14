"""
Problem: Largest Odd Number in String
Platform: LeetCode
Link: https://leetcode.com/problems/largest-odd-number-in-string/
Difficulty: Easy

Pattern:
- String
- Greedy

Approach:
Traverse the string from right to left to find the first odd digit.
Return the substring from the beginning up to that digit.
If no odd digit exists, return an empty string.

Time Complexity: O(n)
Space Complexity: O(1)
"""  

def Odd_number(nums):
    n=len(nums)
    for i in range(n-1,-1,-1):
        if int(nums[i])%2==1:
            return nums[:i+1]
    return ""

#Test case
nums = "52"
print(Odd_number(nums))
