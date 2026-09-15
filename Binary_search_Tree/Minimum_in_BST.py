"""
Problem: Minimum Value in a Binary Search Tree
Platform: GeeksforGeeks
Difficulty: Easy

Pattern:
- Binary Search Tree
- Iteration
- BST Property

BST Property:
    Left < Root < Right

Approach:
In a BST, the minimum value is always present
at the leftmost node.

Start from the root and keep moving to the left
until there is no left child.

The node we stop at contains the minimum value.

Time Complexity: O(h)
Space Complexity: O(1)

where h = height of the BST.
"""

"""
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def minValue(self, root):
        temp=root
        while temp is not None and temp.left is not None:
            temp=temp.left
        return temp.data