"""
Problem: Max Consecutive Ones III
Platform: LeetCode
Problem Number: 1004
Difficulty: Medium

Pattern:
- Sliding Window
- Two Pointers

Approach:
Maintain a sliding window containing at most k zeros.

1. Move the right pointer to expand the window.
2. If nums[right] is 0, increase the zero count.
3. If the number of zeros becomes greater than k,
   move the left pointer until the window becomes valid.
4. After the window is valid, calculate its length.
5. Keep track of the maximum length.

The window represents a subarray in which at most k zeros
can be changed into ones.

Time Complexity: O(n)
Space Complexity: O(1)
"""
def max_ones(nums,k):
    maxi=0
    left=0
    zeros=0
    n=len(nums)
    for right in range(0,n):
        if nums[right]==0:
            zeros+=1
        while zeros>k:
            if nums[left]==0:
                zeros-=1
            left+=1
        maxi=max(maxi,right-left+1)
    return maxi 
#Test case
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(max_ones(nums,k))