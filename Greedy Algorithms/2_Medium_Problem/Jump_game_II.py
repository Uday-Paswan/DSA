"""
Problem: Jump Game II
Platform: LeetCode
Problem Number: 45
Difficulty: Medium

Pattern:
- Greedy
- Array

Approach:
Use a greedy approach to find the minimum number of jumps
needed to reach the last index.

Maintain three variables:
- jumps    → number of jumps made
- current  → farthest index reachable using the current jump
- farthest → farthest index reachable from all positions
             within the current range

For every index:
1. Update farthest using i + nums[i].
2. When we reach the end of the current range,
   we must make another jump.
3. Set current = farthest.

This treats all positions reachable within the current jump
as one range and chooses the next range that extends farthest.

Time Complexity: O(n)
Space Complexity: O(1)
"""
def jump_game_II(nums):
    farthest=0
    jump=0
    current_end=0
    for i in range(len(nums)-1):
        farthest=max(farthest,i+nums[i])
        if i==current_end:
            jump+=1
            current_end=farthest
    return jump

#Test case
nums = [2,3,1,1,4]
print(jump_game_II(nums))