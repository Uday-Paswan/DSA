"""
Problem: Number of Enclaves
Platform: LeetCode
Link: https://leetcode.com/problems/number-of-enclaves/
Difficulty: Medium

Pattern:
- Graph
- Multi-source BFS
- Boundary Traversal

Approach:
Start BFS from all boundary land cells (1).
Mark every land cell connected to the boundary as visited.
These cells can reach the boundary, so they are not enclaves.
Finally, count all land cells that remain unvisited.

Time Complexity: O(R * C)
Space Complexity: O(R * C)
"""

from collections import deque

class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        queue = deque()
        count = 0

        # Add land cells from the first row
        for c in range(cols):
            if grid[0][c] == 1 and visited[0][c] == 0:
                queue.append((0, c))
                visited[0][c] = 1

        # Add land cells from the last column
        for r in range(rows):
            if grid[r][cols - 1] == 1 and visited[r][cols - 1] == 0:
                queue.append((r, cols - 1))
                visited[r][cols - 1] = 1

        # Add land cells from the first column
        for r in range(rows):
            if grid[r][0] == 1 and visited[r][0] == 0:
                queue.append((r, 0))
                visited[r][0] = 1

        # Add land cells from the last row
        for c in range(cols):
            if grid[rows - 1][c] == 1 and visited[rows - 1][c] == 0:
                queue.append((rows - 1, c))
                visited[rows - 1][c] = 1

        # Perform BFS from all boundary land cells
        while queue:
            i, j = queue.popleft()

            # Check all four adjacent directions
            for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_i = i + x
                new_j = j + y

                # Skip cells outside the grid
                if new_i < 0 or new_j < 0 or new_i >= rows or new_j >= cols:
                    continue

                # Skip water cells and already visited cells
                if grid[new_i][new_j] == 0 or visited[new_i][new_j] == 1:
                    continue

                # Mark the land cell visited before adding it to the queue
                visited[new_i][new_j] = 1
                queue.append((new_i, new_j))

        # Count land cells that cannot reach the boundary
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and visited[r][c] == 0:
                    count += 1

        return count