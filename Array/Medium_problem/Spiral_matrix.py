"""
Problem: Spiral Matrix
Platform: LeetCode
Link: https://leetcode.com/problems/spiral-matrix/
Difficulty: Medium

Pattern:
- Matrix
- Simulation

Approach:
Traverse the matrix layer by layer using four boundaries:
top, bottom, left, and right.
After traversing each side, update the corresponding boundary
until all elements are visited.

Time Complexity: O(m × n)
Space Complexity: O(1)
"""
def spiral_matrix(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    top,left=0,0
    bottom=rows-1
    right=cols-1
    result=[]
    while top<=bottom and left<=right:
        for i in range(left,right+1):
            result.append(matrix[top][i])
        top+=1
        for i in range(top,bottom+1):
            result.append(matrix[i][right])
        right-=1
        if top<=bottom:
            for i in range(right,left-1,-1):
                result.append(matrix[bottom][i])
            bottom-=1
        if left<=right:
            for i in range(bottom,top-1,-1):
                result.append(matrix[i][left])
            left+=1
    return result

#Test case
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiral_matrix(matrix))
