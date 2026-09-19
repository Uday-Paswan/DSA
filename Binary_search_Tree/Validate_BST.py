"""
Problem: Validate Binary Search Tree
Platform: LeetCode
Problem Number: 98
Difficulty: Medium

Pattern:
- Binary Search Tree
- Inorder Traversal
- DFS
- Recursion

Key Property:
Inorder traversal of a valid BST produces values
in STRICTLY increasing order.

Approach:
1. Perform inorder traversal: Left → Root → Right.
2. Keep track of the previous visited value.
3. For every node, compare the current value with
   the previous value.
4. If current value <= previous value, the tree is
   not a valid BST.
5. Otherwise continue.

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
    def isValidBST(self, root: TreeNode | None) -> bool:

        prev = None

        def solve(node):
            nonlocal prev

            if node is None:
                return True

            if not solve(node.left):
                return False

            if prev is not None and node.val <= prev:
                return False

            prev = node.val

            return solve(node.right)

        return solve(root)
        