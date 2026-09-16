"""
Problem: Floor in BST
Platform: GeeksforGeeks
Difficulty: Medium

Pattern:
- Binary Search Tree
- BST Property
- Iteration

Definition:
Floor of x = the largest value in the BST
that is less than or equal to x.

Approach:
Start from the root.

1. If node.data == x:
   x itself is the floor → return x.

2. If x > node.data:
   Current node can be a possible floor.
   Move RIGHT to find a larger value that is still <= x.

3. If x < node.data:
   Current node is too large, so it cannot be the floor.
   Move LEFT.

Keep track of the possible floor.

Time Complexity: O(h)
Space Complexity: O(1)
"""
'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxFork(self, root, k):
        #code here
        if root is None:
            return None
        temp=root
        floor=-1
        while temp is not None:
            if k==temp.data:
                return temp.data
            elif k<temp.data:
                temp=temp.left
            else:
                floor=temp.data
                temp=temp.right
        return floor