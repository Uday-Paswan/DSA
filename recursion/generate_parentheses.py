"""
Problem: Generate Parentheses
Platform: LeetCode
Link: https://leetcode.com/problems/generate-parentheses/
Difficulty: Medium

Pattern:
- Backtracking
- Recursion

Approach:
Generate all valid combinations by maintaining two counters:
1. open_used  -> Number of '(' used so far.
2. close_used -> Number of ')' used so far.

Rules:
- Add '(' only if open_used < n.
- Add ')' only if close_used < open_used.

When the current string length becomes 2 * n, a valid
combination is formed. Add it to the result.

Time Complexity: O(4^n / √n)   (Catalan Number)
Space Complexity: O(n) (excluding the output)
"""
def generate_parentheses(n):
    result=[]
    def backtrack(current,open,close):
        if len(current)==2*n:
            result.append("".join(current))
            return
        if open<n:
            backtrack(current + "(",open+1,close)
        if close<open:
            backtrack(current + ")",open,close+1)
    backtrack("",0,0)
    return result
#Test case
n = 3
print(generate_parentheses(n))