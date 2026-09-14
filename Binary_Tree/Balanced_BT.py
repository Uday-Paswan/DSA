"""
Problem: Balanced Binary Tree
Platform: LeetCode
Problem Number: 110
Difficulty: Easy

Pattern:
- Binary Tree
- DFS
- Recursion
- Height of Binary Tree

Definition:
A binary tree is balanced if, for every node, the difference
between the height of its left and right subtrees is at most 1.

Approach:
Use DFS to calculate the height of each subtree.

1. If node is None, return height 0.
2. Find the height of the left subtree.
3. Find the height of the right subtree.
4. If the difference between the two heights is greater than 1,
   the tree is not balanced.
5. Return the height of the current subtree.

Optimization:
If an unbalanced subtree is found, return -1 immediately.
This avoids repeatedly checking the same subtrees.

Time Complexity: O(n)
Space Complexity: O(h)
where h = height of the tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def solve(node):
            if node==None:
                return 0
            leftheight=solve(node.left)
            if leftheight==-1:
                return -1
            rightheight=solve(node.right)
            if rightheight==-1:
                return -1
            if abs(leftheight-rightheight)>1:
                return -1
            return 1 +max(leftheight,rightheight)
        x=solve(root)
        if x==-1:
            return False
        return True