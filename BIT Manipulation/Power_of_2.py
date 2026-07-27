"""
Problem: Power of Two
Platform: LeetCode
Link: https://leetcode.com/problems/power-of-two/
Difficulty: Easy

Pattern:
- Bit Manipulation
- Math

Approach:
A power of two has exactly one set bit in its binary
representation. If n > 0 and (n & (n - 1)) == 0,
then n is a power of two; otherwise, it is not.

Time Complexity: O(1)
Space Complexity: O(1)
"""

def power(n):
    if n>0:
        if n&(n-1)==0:
            return True
        else:
            return False
    return False

#Test Case
n=9
print(power(n))