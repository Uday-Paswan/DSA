"""
Problem: Rat in a Maze
Platform: GeeksforGeeks
Difficulty: Medium

Pattern:
- Backtracking
- Recursion
- Matrix / 2D Array

Approach:
Start from the top-left cell and try moving in all four
directions: Down, Left, Right, and Up.

A cell can be visited only if:
1. It is inside the matrix.
2. It is not blocked.
3. It has not already been visited.

When the rat reaches the bottom-right cell, store the path.

Time Complexity: O(4^(n²)) in the worst case
Space Complexity: O(n²)
"""
def ratInMaze(maze):

        n = len(maze)
        ans = []
        path = []

        if maze[0][0] == 0 or maze[n - 1][n - 1] == 0:
            return ans

        visited = [[False] * n for _ in range(n)]

        dr = [1, 0, 0, -1]
        dc = [0, -1, 1, 0]
        direction = ["D", "L", "R", "U"]

        def solve(row, col):

            if row == n - 1 and col == n - 1:
                ans.append("".join(path))
                return

            for i in range(4):

                new_row = row + dr[i]
                new_col = col + dc[i]

                if (0 <= new_row < n and
                    0 <= new_col < n and
                    maze[new_row][new_col] == 1 and
                    not visited[new_row][new_col]):

                    visited[new_row][new_col] = True
                    path.append(direction[i])

                    solve(new_row, new_col)

                    path.pop()
                    visited[new_row][new_col] = False

        visited[0][0] = True
        solve(0, 0)

        return ans
#Test Case
maze= [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
print(ratInMaze(maze))
