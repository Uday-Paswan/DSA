"""
Problem: Maximum Depth of Binary Tree
Platform: LeetCode
Problem Number: 104
Difficulty: Easy

Pattern:
- Binary Tree
- DFS
- Recursion

Approach:
For every node, recursively find the depth of its
left and right subtrees.

1. Base case:
   If node is None, return 0.

2. Recursively find:
   left_depth  = depth of left subtree
   right_depth = depth of right subtree

3. The current node contributes 1 level, so return:

   1 + max(left_depth, right_depth)

Time Complexity: O(n)
Space Complexity: O(h)
where h = height of the tree because of the recursion stack.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def solve(node):
            if node==None:
                return 0
            leftheight=solve(node.left)
            rightheight=solve(node.right)
            return 1+max(leftheight,rightheight)
        return solve(root)