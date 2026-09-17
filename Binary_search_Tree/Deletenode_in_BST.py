"""
Problem: Delete Node in a Binary Search Tree
Platform: LeetCode
Problem Number: 450
Difficulty: Medium

Pattern:
- Binary Search Tree
- Recursion

BST Property:
    Left < Root < Right

Cases while deleting:
1. Node not found:
       return root

2. Node is a leaf:
       return None

3. Node has only right child:
       return root.right

4. Node has only left child:
       return root.left

5. Node has two children:
       Find the inorder successor (smallest value
       in the right subtree).
       Replace current node's value with successor's value.
       Delete the successor from the right subtree.

Time Complexity: O(h)
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
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if root is None:
            return None
        if root.val==key:
            return self.deletion(root)
        temp=root
        while temp is not None:
            if key<temp.val:
                if temp.left is not None and key==temp.left.val:
                    temp.left=self.deletion(temp.left)
                    break
                else:
                    temp=temp.left
            else:
                if temp.right is not None and key==temp.right.val:
                    temp.right=self.deletion(temp.right)
                    break
                else:
                    temp=temp.right
        return root

    def deletion(self,node):
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            right_child=node.right
            last_right=self.findlastright(node.left)
            last_right.right=right_child
            return node.left

    def findlastright(self,node):
        while node.right is not None:
            node=node.right
        return node