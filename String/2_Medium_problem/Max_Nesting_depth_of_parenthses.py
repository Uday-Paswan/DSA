"""
Problem: Maximum Nesting Depth of the Parentheses
Platform: LeetCode
Link: https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/
Difficulty: Easy

Pattern:
- String
- Stack (Counter)

Approach:
Traverse the string while maintaining a counter for the current
nesting depth. Increment the counter when '(' is encountered and
decrement it when ')' is encountered. Update the maximum depth
whenever the current depth increases.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def depth(s):
    balance=0
    max_depth=0
    for ch in s:
        if ch=="(":
            balance+=1
            max_depth=max(max_depth,balance)
        elif ch==")":
            balance-=1
    return max_depth

#Test case
s = "()(())((()()))"
print(depth(s))