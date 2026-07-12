"""
Problem: Valid Anagram
Platform: LeetCode
Link: https://leetcode.com/problems/valid-anagram/
Difficulty: Easy

Pattern:
- String
- Hash Map

Approach:
Count the frequency of each character in the first string
using a hash map. Then decrement the count while traversing
the second string. If all counts become zero, the strings
are valid anagrams.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def anagram(s,t):
    freq={}
    if len(s)!=len(t):
        return False
    for c in s:
        if c in freq:
            freq[c]+=1
        else:
            freq[c]=1
    for c in t:
        if c not in freq:
            return False
        freq[c]-=1
        if freq[c]<0:
            return False
    return True

#Test case
s="a,b,c"
t="a,b,d"
print(anagram(s,t))