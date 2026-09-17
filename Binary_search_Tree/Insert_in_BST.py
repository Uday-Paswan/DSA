"""
Problem: Insert a Node in a Binary Search Tree
Pattern: Binary Search Tree
Difficulty: Medium

BST Property:
    left < root < right

Approach:
1. If the root is None, create and return a new node.
2. Compare the value with the current node.
3. If value < node.val:
       insert into the left subtree.
4. If value > node.val:
       insert into the right subtree.
5. Return the root.

Time Complexity: O(h)
Space Complexity: O(h) for recursion

where h = height of the BST.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if root is None:
            return TreeNode(val)
        temp=root
        while True:
            if val<temp.val:
                if temp.left is None:
                    temp.left=TreeNode(val)
                    break
                temp=temp.left
            else:
                if temp.right is None:
                    temp.right=TreeNode(val)
                    break
                temp=temp.right
        return root