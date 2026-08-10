"""
Problem: Letter Combinations of a Phone Number
Platform: LeetCode
Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Difficulty: Medium

Pattern:
- Backtracking
- Recursion

Approach:
Map each digit to its corresponding letters on a phone keypad.
For every digit, recursively choose each possible letter and move
to the next digit.

When all digits have been processed, add the current combination
to the result.

Time Complexity: O(4^n)
Space Complexity: O(n) excluding the output
"""

def combination(digits):
    result=[]
    subset=[]
    mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
             }
    def solve(index):
        if index==len(digits):
            result.append("".join(subset))
            return
        letters=mapping[digits[index]]
        for ch in letters:
            subset.append(ch)
            solve(index+1)
            subset.pop()
    solve(0)
    return result
#Test case
digits = "23"
print(combination(digits))