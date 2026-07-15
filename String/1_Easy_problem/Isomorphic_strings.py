"""
Problem: Isomorphic Strings
Platform: LeetCode
Link: https://leetcode.com/problems/isomorphic-strings/
Difficulty: Easy

Pattern:
- String
- Hash Map

Approach:
Maintain a one-to-one mapping between the characters of both
strings. While traversing the strings, ensure that each character
consistently maps to the same character and that no two different
characters map to the same character.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def is_isomorphic(s,t):
    s_t={}
    t_s={}
    for i in range(len(s)):
        if s[i] in s_t:
            if s_t[s[i]]!=t[i]:
                return False
        if t[i] in t_s:
            if t_s[t[i]]!=s[i]:
                return False
        s_t[s[i]]=t[i]
        t_s[t[i]]=s[i]
    return True

#Test Case
s = "paper"
t = "title"
print(is_isomorphic(s,t))