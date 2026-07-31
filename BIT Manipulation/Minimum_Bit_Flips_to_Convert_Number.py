"""
Problem: Minimum Bit Flips to Convert Number
Platform: LeetCode
Link: https://leetcode.com/problems/minimum-bit-flips-to-convert-number/
Difficulty: Easy

Pattern:
- Bit Manipulation
- XOR

Approach:
XOR the start and goal numbers to identify the bits that differ.
Each set bit (1) in the XOR result represents one bit that must
be flipped. Count the number of set bits and return the count.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def flip_bit(start,goal):
    ans=start^goal
    count=0
    while ans:
        ans=ans&(ans-1)
        count+=1
    return count

#Test case
start = 10
goal = 7
print(flip_bit(start,goal))