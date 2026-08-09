"""
Problem: Subset Sum
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1
Difficulty: Medium

Pattern:
- Recursion
- Backtracking
- Pick / Not Pick

Approach:
For every element, make two choices:
1. Pick the current element and add it to the current sum.
2. Do not pick the current element.

At the end of the array, check whether the current sum is equal
to the target.

If a valid subset is found, return True.

Time Complexity: O(2^n)
Space Complexity: O(n)
"""
def subset_sum(arr):
    result=[]
    def solve(index,current_sum):
        if index>=len(arr):
            result.append(current_sum)
            return
        solve(index+1,current_sum+arr[index])
        solve(index+1,current_sum)
    solve(0,0)
    return result
#Test case
arr = [2, 3]
print(subset_sum(arr))