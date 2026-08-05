"""
Problem: Print All Subsequences with Sum K
Platform: Recursion Practice

Pattern:
- Recursion
- Backtracking

Approach:
Generate all possible subsequences using recursion. At each index,
make two choices:
1. Pick the current element.
2. Do not pick the current element.

Maintain the current subsequence and its sum. When all elements
have been processed, print the subsequence if its sum equals K.

Time Complexity: O(2^n)
Space Complexity: O(n) (excluding the output)
"""

def printSubsequence(index, arr, subset, current_sum, k):
    # Base Case
    if index == len(arr):
        if current_sum == k:
            print(subset)
        return

    # Pick the current element
    subset.append(arr[index])
    printSubsequence(index + 1, arr, subset, current_sum + arr[index], k)

    # Backtrack
    subset.pop()

    # Not Pick the current element
    printSubsequence(index + 1, arr, subset, current_sum, k)


# Test Case
arr = [1, 2, 1]
k = 2

printSubsequence(0, arr, [], 0, k)
