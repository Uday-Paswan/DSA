"""
Problem: Jump Game
Platform: LeetCode
Problem Number: 55
Difficulty: Medium

Pattern:
- Greedy
- Array

Approach:
Keep track of the farthest index that can be reached.

1. Start with max_reach = 0.
2. Traverse the array.
3. If the current index is greater than max_reach,
   we cannot reach this position, so return False.
4. Update max_reach using:
       max(max_reach, i + nums[i])
5. If max_reach reaches the last index, return True.

Time Complexity: O(n)
Space Complexity: O(1)
"""
def jump_game(nums):
    max_reach=0
    n=len(nums)
    for i in range(n):
        if i>max_reach:
            return False
        max_reach=max(max_reach,i+nums[i])
        if max_reach>=n-1:
            return True
    return True

#Test Case
nums = [3,2,1,0,4]
print(jump_game(nums))