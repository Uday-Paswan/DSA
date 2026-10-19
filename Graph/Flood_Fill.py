"""
Problem: Flood Fill
Platform: LeetCode
Link: https://leetcode.com/problems/flood-fill/
Difficulty: Easy

Pattern:
- Graphs
- Breadth-First Search (BFS)
- Matrix Traversal
- Queue

Approach:
If the starting pixel already has the target color, return
the original image because no changes are needed.

Store the original color of the starting pixel and create
a deep copy of the image to store the updated colors.

Initialize a queue with the starting pixel and mark it with
the target color immediately to prevent duplicate visits.

Use BFS to explore the four adjacent directions:
right, left, down, and up.

Skip neighbors that are outside the image boundaries or
do not have the original color.

For each valid neighbor, change its color before adding it
to the queue. This ensures that each pixel is processed
at most once.

Continue until the queue is empty and return the updated image.

Time Complexity: O(R * C)
Space Complexity: O(R * C)
"""

from collections import deque
from copy import deepcopy


class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:

        # If the starting pixel already has the target color,
        # no changes are required.
        if image[sr][sc] == color:
            return image

        # Store the original color of the starting pixel.
        initial_color = image[sr][sc]

        # Create a copy so the original image remains unchanged.
        vis = deepcopy(image)

        # Get the number of rows and columns.
        row = len(image)
        col = len(image[0])

        # Initialize the BFS queue with the starting pixel.
        queue = deque()
        queue.append((sr, sc))

        # Mark the starting pixel as visited immediately.
        vis[sr][sc] = color

        # Define the four possible movement directions.
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Process pixels until the queue becomes empty.
        while queue:
            i, j = queue.popleft()

            # Explore all four adjacent neighbors.
            for dx, dy in direction:
                new_i, new_j = i + dx, j + dy

                # Skip neighbors outside the image boundaries.
                if new_i < 0 or new_i >= row or new_j < 0 or new_j >= col:
                    continue

                # Skip neighbors that do not have the original color.
                if vis[new_i][new_j] != initial_color:
                    continue

                # Recolor before enqueueing to prevent duplicate visits.
                vis[new_i][new_j] = color
                queue.append((new_i, new_j))

        # Return the updated image.
        return vis