"""
Problem: Set Matrix Zeroes
Platform: LeetCode
Link: https://leetcode.com/problems/set-matrix-zeroes/
Difficulty: Medium

Pattern:
- Matrix
- Simulation
- In-place

Approach:
Use the first row and first column as markers to identify
which rows and columns should be set to zero.
Finally, update the matrix based on these markers.

Time Complexity: O(m × n)
Space Complexity: O(1)
"""
def set_martix_zero(matrix):
    r=len(matrix)
    c=len(matrix[0])
    rows=set()
    cols=set()
    for i in range(r):
        for j in range(c):
            if matrix[i][j]==0:
                rows.add(i)
                cols.add(j)
    for i in range(r):
        for j in range(c):
            if i in rows or j in cols:
                matrix[i][j]=0
    return(matrix)

#Test case 
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(set_martix_zero(matrix))