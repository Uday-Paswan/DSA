"""
Problem: Top View of Binary Tree
Platform: GeeksforGeeks
Difficulty: Medium

Pattern:
- Binary Tree
- BFS
- Queue
- HashMap / Dictionary
- Horizontal Distance

Approach:
Assign every node a Horizontal Distance (HD).

Rules:
- Root has HD = 0
- Left child has HD = HD - 1
- Right child has HD = HD + 1

Use BFS so that nodes are processed level by level.

For each HD:
- Store the first node encountered.
- Ignore later nodes having the same HD.

Finally, sort the horizontal distances and print the
corresponding values from left to right.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    def topView(self, root):
        # code here
        queue=deque([(root,0)])
        ans=[]
        top={}
        while queue:
            node,HD=queue.popleft()
            if HD not in top:
                top[HD]=node.data
            if node.left is not None:
                queue.append((node.left,HD-1))
            if node.right is not None:
                queue.append((node.right,HD+1))
        for value in sorted(top.items()):
            ans.append(value[1])
        return ans