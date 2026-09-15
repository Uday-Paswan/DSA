"""
Problem: Search in a Binary Search Tree
Platform: LeetCode
Problem Number: 700
Difficulty: Easy

Pattern:
- Binary Search Tree
- BST Property
- Iteration

BST Property:
    left subtree < root < right subtree

Approach:
Start from the root.

For every node:
- If node.val == val → target found, return node.
- If val < node.val → target must be in the left subtree.
- If val > node.val → target must be in the right subtree.

We don't need to search both sides because the BST
property tells us which side can contain the target.

If we reach None, the value doesn't exist.

Time Complexity: O(h)
Space Complexity: O(1)

where h = height of the BST.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp=root
        while temp is not None:
            if temp.val==val:
                return temp
            elif val<temp.val:
                temp=temp.left
            else:
                temp=temp.right
        return None