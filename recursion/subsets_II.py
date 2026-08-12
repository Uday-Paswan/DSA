"""
Problem: Subsets II
Platform: LeetCode
Link: https://leetcode.com/problems/subsets-ii/
Difficulty: Medium

Pattern:
- Backtracking
- Recursion
- Sorting
- Duplicate Handling

Approach:
Sort the array first so that duplicate elements become adjacent.
Generate subsets using backtracking.

At each recursion level, skip a duplicate element if it is the
same as the previous element and is not the first choice at that
level. This prevents generating duplicate subsets.

Time Complexity: O(n * 2^n)
Space Complexity: O(n) excluding the output
"""
def subset(nums):
    result=[]
    subset=[]
    nums.sort()
    def solve(index):
        result.append(subset.copy())
        for i in range(index,len(nums)):
            if i>index and nums[i]==nums[i-1]:
                continue
            subset.append(nums[i])
            solve(i+1)
            subset.pop()
    solve(0)
    return result

#Test Case
nums = [1,2,2]
print(subset(nums))