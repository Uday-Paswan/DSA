"""
Problem: N-Queens
Platform: LeetCode
Link: https://leetcode.com/problems/n-queens/
Difficulty: Hard

Pattern:
- Backtracking
- Recursion
- Matrix / 2D Array

Approach:
Place one queen in each row. For every row, try placing the
queen in each column.

Before placing a queen, check whether the position is safe:
1. Same column
2. Upper-left diagonal
3. Upper-right diagonal

If the position is safe, place the queen and recursively move
to the next row. After returning, remove the queen and try the
next column.

When all n rows are completed, store the board configuration.

Time Complexity: O(n!)
Space Complexity: O(n^2) excluding the output
"""

def n_queens(n):
    ans=[]
    board=["."*n for _ in range(n)]
    leftrow=[0]*n
    lower_dia=[0]*(2*n-1)
    upper_dia=[0]*(2*n-1)
    def solve(col,board,ans,leftrow,lower_dia,upper_dia):
        if col==n:
            ans.append(board[:])
            return
        for row in range(n):
            if(leftrow[row]==0 and lower_dia[row+col]==0 and upper_dia[n-1+col-row]==0):
                board[row]=board[row][:col]+"Q"+ board[row][col+1:]
                leftrow[row]=1
                lower_dia[row+col]=1
                upper_dia[n-1+col-row]=1
                solve(col+1,board,ans,leftrow,lower_dia,upper_dia)
                board[row]=board[row][:col]+"."+ board[row][col+1:]
                leftrow[row]=0
                lower_dia[row+col]=0
                upper_dia[n-1+col-row]=0
    solve(0,board,ans,leftrow,lower_dia,upper_dia)
    return ans

#Test case
n=4
print(n_queens(n))