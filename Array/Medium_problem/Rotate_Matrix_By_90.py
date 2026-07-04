"""
Problem: Rotate Image
Platform: LeetCode
Link: https://leetcode.com/problems/rotate-image/
Difficulty: Medium

Pattern:
- Matrix
- In-place
- Transpose

Approach:
Transpose the matrix by swapping rows and columns.
Then reverse each row to rotate the matrix 90 degrees clockwise.

Time Complexity: O(n²)
Space Complexity: O(1)
"""
def rotate_matrix(matrix):
    r=len(matrix)
    c=len(matrix[0])
    for i in range(r):
        for j in range(i+1,c):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

    for i in range(r):
        left=0
        right=c-1
        while left<right:
            matrix[i][left],matrix[i][right]=matrix[i][right],matrix[i][left] #matrix[i].reverse()
            left+=1
            right-=1
    return matrix

#Test case
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate_matrix(matrix))