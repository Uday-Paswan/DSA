"""
Problem: Combination Sum III
Platform: LeetCode
Link: https://leetcode.com/problems/combination-sum-iii/
Difficulty: Medium

Pattern:
- Backtracking
- Recursion
- Combination Generation

Approach:
Choose exactly k distinct numbers from 1 to 9 whose sum equals n.

Start from number 1 and explore numbers up to 9. At each step,
either choose the current number or skip it. Once a number is
chosen, move to the next number so that the same number cannot
be used again.

When k numbers have been selected:
- If their sum equals n, store the combination.
- Otherwise, discard it.

Time Complexity: O(C(9, k))
Space Complexity: O(k) excluding the output
"""

def sum(k,n):
    result=[]
    subset=[]
    def solve(index,k,total):
        if k==0:
            if total==0:
                result.append(subset.copy())
            return
        if total<0:
            return
        for i in range(index,10):
            subset.append(i)
            solve(i+1,k-1,total-i)
            subset.pop()
    solve(1,k,n)
    return result
#Test case
k = 3
n = 9
print(sum(k,n))