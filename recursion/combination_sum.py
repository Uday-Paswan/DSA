"""
Problem: Combination Sum
Platform: LeetCode
Link: https://leetcode.com/problems/combination-sum/
Difficulty: Medium

Pattern:
- Backtracking
- Recursion
- Pick / Not Pick

Approach:
At each index, make two choices:
1. Pick the current candidate and stay at the same index because
   the same number can be used unlimited times.
2. Don't pick the current candidate and move to the next index.

When the target becomes 0, store a copy of the current combination.
If the target becomes negative, stop exploring that branch.

Time Complexity: O(2^n) approximately
Space Complexity: O(target) for recursion/combination storage
"""
def combination_sum(candidates,target):
    result=[]
    subset=[]
    def solve(index,target):
        if target==0:
            result.append(subset.copy())
            return
        if index==len(candidates) or target<0:
            return
        subset.append(candidates[index])
        solve(index,target-candidates[index])
        subset.pop()
        solve(index+1,target)
    solve(0,target)
    return result

#Test case
candidates = [2,3,6,7]
target = 7
print(combination_sum(candidates,target))