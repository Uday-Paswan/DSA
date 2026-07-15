"""
Problem: Remove Outermost Parentheses
Platform: LeetCode
Link: https://leetcode.com/problems/remove-outermost-parentheses/
Difficulty: Easy

Pattern:
- String
- Stack

Approach:
Traverse the string while maintaining the current nesting depth.
Skip the first opening parenthesis of each primitive substring
and the last closing parenthesis of each primitive substring.
Append all remaining parentheses to the result.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def remove(s):
    balance=0
    result=""
    for ch in s:
        if ch=="(":
            if balance>0:
                result+=ch
            balance+=1
        else:
            balance-=1
            if balance>0:
                result+=ch
    return result

#Test Case
s = "(()())(())(()(()))"
print(remove(s))