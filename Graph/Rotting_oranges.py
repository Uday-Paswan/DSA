"""
Problem: Rotting Oranges
Platform: LeetCode
Link: https://leetcode.com/problems/rotting-oranges/
Difficulty: Medium

Pattern:
- Graphs
- Breadth-First Search (BFS)
- Multi-Source BFS
- Matrix Traversal

Approach:
Add all initially rotten oranges (2) to the queue and count
the number of fresh oranges (1).

Use Multi-Source BFS to spread rot from all rotten oranges
simultaneously.

Process the queue level by level, where each level represents
one minute.

For each rotten orange, check its four adjacent cells:
up, down, left, and right.

If an adjacent cell contains a fresh orange:
- Change its value to 2 (rotten).
- Decrease the fresh orange count.
- Add its position to the queue.

Increase time after processing each BFS level.

If fresh oranges remain after BFS, return -1.
Otherwise, return the total time taken.

Time Complexity: O(R * C)
Space Complexity: O(R * C)
"""
from collections import deque 
from copy import deepcopy
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        fresh_count=0
        minutes=0
        grid_copy=deepcopy(grid)
        queue=deque()
        rows=len(grid)
        col=len(grid[0])
        for r in range(rows):
            for c in range(col):
                if grid_copy[r][c]==2:
                    queue.append((r,c))
                elif grid_copy[r][c]==1:
                    fresh_count+=1
        direction=[(0,1),(1,0),(-1,0),(0,-1)]
        while len(queue)!=0 and fresh_count>0:
            minutes+=1
            rotten=len(queue)
            for _ in range(rotten):
                i,j=queue.popleft()
                for dx,dy in direction:
                    new_i,new_j=i+dx,j+dy
                    if new_i<0 or new_j<0 or new_i==rows or new_j==col:
                        continue
                    if grid_copy[new_i][new_j]==0 or grid_copy[new_i][new_j]==2:
                        continue
                    fresh_count-=1
                    queue.append((new_i,new_j))
                    grid_copy[new_i][new_j]=2
        if fresh_count>0:
            return -1
        return minutes

