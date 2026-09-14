"""
Problem: Bottom View of Binary Tree
Platform: GeeksforGeeks
Difficulty: Medium

Pattern:
- Binary Tree
- BFS
- Queue
- HashMap / Dictionary
- Horizontal Distance

Approach:
Assign a Horizontal Distance (HD) to every node.

Rules:
- Root → HD = 0
- Left child → HD - 1
- Right child → HD + 1

Use BFS (level-order traversal).

For every node:
- Store/update the node's value at its horizontal distance.
- Since BFS processes nodes level by level, a later node at
  the same HD will be lower in the tree, so it replaces the
  previous value.

Finally, sort the horizontal distances and return their values
from left to right.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''
from collections import deque
class Solution:
    def bottomView(self, root):
        # code here
        queue=deque([(root,0)])
        if root is None:
            return 
        bottom={}
        ans=[]
        while queue:
            node,hd=queue.popleft()
            
            bottom[hd]=node.data
                
            if node.left is not None:
                queue.append((node.left,hd-1))
            if node.right is not None:
                queue.append((node.right,hd+1))
        for hd in sorted(bottom):
            ans.append(bottom[hd])
        return ans