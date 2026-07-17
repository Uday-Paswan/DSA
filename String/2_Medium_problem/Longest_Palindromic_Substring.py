"""
Problem: Longest Palindromic Substring
Platform: LeetCode
Link: https://leetcode.com/problems/longest-palindromic-substring/
Difficulty: Medium

Pattern:
- String
- Two Pointers

Approach:
Treat each character (and the gap between two characters) as the
center of a palindrome. Expand outward while the characters on
both sides are equal and keep track of the longest palindrome found.

Time Complexity: O(n²)
Space Complexity: O(1)
"""
def longest_palindrome(s):
    n=len(s)
    ans=""
    def expand(left,right):
        while left>=0 and right<n and s[left]==s[right]:
                left-=1
                right+=1
        return s[left+1:right]

    for i in range(n):
        odd=expand(i,i)
        even=expand(i,i+1)
        if len(odd)>len(ans):
            ans = odd
        if len(even)>len(ans):
            ans = even 
    return ans

#Test Case
s = "racecar"
print(longest_palindrome(s))