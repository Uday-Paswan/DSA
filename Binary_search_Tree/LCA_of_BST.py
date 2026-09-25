"""
Problem: Lowest Common Ancestor of a Binary Search Tree
Platform: LeetCode
Problem Number: 235
Difficulty: Medium

Pattern:
- Binary Search Tree
- Tree
- Iteration

BST Property:
    Left < Root < Right

Approach:
For the current node:

1. If both p and q are smaller than current:
       LCA must be in the LEFT subtree.

2. If both p and q are greater than current:
       LCA must be in the RIGHT subtree.

3. Otherwise:
       Current node is the LCA.

This works because the first node where p and q
split into different directions is their LCA.

Time Complexity: O(h)
Space Complexity: O(1)
where h = height of the BST.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:

            if p.val < root.val and q.val < root.val:
                root = root.left

            elif p.val > root.val and q.val > root.val:
                root = root.right

            else:
                return root