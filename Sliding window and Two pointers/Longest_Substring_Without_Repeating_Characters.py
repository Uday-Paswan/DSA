"""
Problem: Longest Substring Without Repeating Characters
Platform: LeetCode
Problem Number: 3
Difficulty: Medium

Pattern:
- Sliding Window
- Two Pointers
- Hash Set / Hash Map

Approach:
Use two pointers, left and right, to maintain a sliding window
containing only unique characters.

1. Move the right pointer through the string.
2. If the current character is not in the window, add it.
3. If the character is already present, move the left pointer
   until the duplicate character is removed.
4. Calculate the current window length.
5. Keep track of the maximum length.

Time Complexity: O(n)
Space Complexity: O(n)
"""
def lengthOfLongestSubstring(s):
    maxi=0
    left=0
    right=0
    my_dict={}
    n=len(s)

    while right<n:
        if s[right] in my_dict:
            left=max(left,my_dict[s[right]]+1)
        maxi=max(maxi,right-left+1)
        my_dict[s[right]]=right
        right+=1
    return maxi

#Test Case
s = "bbbbb"
print(lengthOfLongestSubstring(s))