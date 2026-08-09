"""
Problem: Combination Sum II
Platform: LeetCode
Link: https://leetcode.com/problems/combination-sum-ii/
Difficulty: Medium

Pattern:
- Backtracking
- Recursion
- Sorting
- Duplicate Handling

Approach:
Sort the candidates first. At each recursion level, choose an
element and move to the next index because each element can be
used only once.

Skip duplicate values at the same recursion level to avoid
generating duplicate combinations.

If the remaining target becomes 0, store the current combination.
If the remaining target becomes negative, stop exploring that
branch.

Time Complexity: O(2^n) approximately
Space Complexity: O(n) excluding the output
"""

def sum (candidates,target):
    result=[]
    subset=[]
    candidates.sort()
    def solve(index,target):
        if target==0:
            result.append(subset.copy())
            return
        if index==len(candidates) or target<0:
            return
        for i in range(index,len(candidates)):
            if i>index and candidates[i]==candidates[i-1]:
                continue 
            subset.append(candidates[i])
            solve(i+1,target-candidates[i])
            subset.pop()
    solve(0,target)
    return result

#Test case
candidates = [10,1,2,7,6,1,5]
target = 8
print(sum(candidates,target))

    


            
                    