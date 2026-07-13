"""
Problem: Longest Common Prefix
Platform: LeetCode
Link: https://leetcode.com/problems/longest-common-prefix/
Difficulty: Easy

Pattern:
- String

Approach:
Take the first string as the initial prefix.
Compare it character by character with every other string.
Stop when a mismatch is found and return the common prefix.

Time Complexity: O(n × m)
Space Complexity: O(1)
"""

def common_prefix(strs):
    first=strs[0]
    prefix=""
    for i in range(len(first)):
        for j in range(1,len(strs)):
            if i>len(strs[j]):
                return prefix
            if strs[j][i]!=first[i]:
                return prefix
        prefix+=first[i]
    return prefix

#Test Case
strs = ["dog","racecar","car"]
print(common_prefix(strs))