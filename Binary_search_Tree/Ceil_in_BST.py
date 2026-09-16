"""
Problem: Ceil in BST
Platform: GeeksforGeeks
Difficulty: Medium

Pattern:
- Binary Search Tree
- BST Property
- Iteration

Definition:
Ceil of x = the smallest value in the BST
that is greater than or equal to x.

Approach:
Start from the root.

1. If node.data == x:
   x itself is the ceil → return x.

2. If x < node.data:
   Current node can be a possible ceil.
   Move LEFT to find a smaller value that is still >= x.

3. If x > node.data:
   Current node is too small, so it cannot be the ceil.
   Move RIGHT.

Keep track of the possible ceil.

Time Complexity: O(h)
Space Complexity: O(1)
"""
'''
Definition for Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 
'''
        
class Solution:
    def findCeil(self,root, x):
        # code here
        if root is None:
            return None
        ceil=-1
        temp=root
        while temp is not None:
            if temp.data==x:
                return temp.data
            elif x<temp.data:
                ceil=temp.data
                temp=temp.left
            else:
                temp=temp.right
        return ceil