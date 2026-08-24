"""
Problem: Pow(x, n)
Platform: LeetCode
Problem Number: 50
Difficulty: Medium

Pattern:
- Recursion
- Divide and Conquer
- Binary Exponentiation

Goal:
Calculate x^n efficiently.

Important:
We should NOT multiply x, n times because that gives O(n)
time complexity.

Instead, use the following idea:

If n is even:
    x^n = (x^(n/2)) * (x^(n/2))

If n is odd:
    x^n = x * x^(n-1)

Time Complexity: O(log n)
Space Complexity: O(log n) for recursive solution
"""

def pow(x,n):
    if n==0:
        return 1
    if n<0:
        return 1/pow(x,-n)
    half=pow(x,n//2)
    if n%2==0:
        return half*half
    return x*half*half
#Test case
x = 2.00000
n = 10
print(pow(x,n))