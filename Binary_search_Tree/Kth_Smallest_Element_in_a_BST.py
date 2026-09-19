"""
Problem: Kth Smallest Element in a BST
Platform: LeetCode
Problem Number: 230
Difficulty: Medium

Pattern:
- Binary Search Tree
- Inorder Traversal
- DFS
- Recursion

Key Property:
Inorder traversal of a BST gives values in sorted order.

Approach:
1. Perform inorder traversal: Left → Root → Right.
2. Maintain a count of visited nodes.
3. When count becomes equal to k, we found the
   kth smallest element.
4. No need to store all values in a list.

Time Complexity: O(n)
Space Complexity: O(h)

where h = height of the BST.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        count=0
        ans=0
        def solve(root):
            nonlocal count,ans
            if root is None:
                return
            solve(root.left)
            count+=1
            if count==k:
                ans=root.val
            solve(root.right)
        solve(root)
        return ans