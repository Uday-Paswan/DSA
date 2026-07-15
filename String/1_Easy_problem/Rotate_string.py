"""
Problem: Rotate String
Platform: LeetCode
Link: https://leetcode.com/problems/rotate-string/
Difficulty: Easy

Pattern:
- String

Approach:
Concatenate the original string with itself.
If the goal string is a substring of the concatenated string
and both strings have the same length, return True.
Otherwise, return False.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def rotate_string(s,goal):
    if len(s)!=len(goal):
        return False
    double = s + s
    if goal in double:
        return True
    return False

#Test Case
s = "abcde"
goal = "cdeab"
print(rotate_string(s,goal))