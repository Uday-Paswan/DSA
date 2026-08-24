"""
Problem: Count Good Numbers
Platform: LeetCode
Problem Number: 1922
Difficulty: Medium

Pattern:
- Recursion
- Divide and Conquer
- Binary Exponentiation
- Math

Approach:
For even indices, there are 5 possible digits:
0, 2, 4, 6, 8

For odd indices, there are 4 possible digits:
2, 3, 5, 7

Therefore:
Answer = 5^(number of even positions) *
         4^(number of odd positions)

Use binary exponentiation to calculate the powers
efficiently in O(log n) time.

Time Complexity: O(log n)
Space Complexity: O(log n)
"""
def good_number(n):
    MOD=10**9 + 7
    def pow(x,n):
        if n==0:
            return 1
        half=pow(x,n//2)
        if n%2==0:
            return (half*half)%MOD
        return (x*half*half)%MOD
    even=(n+1)//2
    odd=n//2
    return (pow(5,even)*pow(4,odd))%MOD
#Test Case
n=5
print(good_number(n))