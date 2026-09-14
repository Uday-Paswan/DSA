"""
Problem: Binary Tree Right Side View
Platform: LeetCode
Problem Number: 199
Difficulty: Medium

Pattern:
- Binary Tree
- DFS
- Recursion
- Preorder Traversal

Approach:
Use DFS and visit the RIGHT subtree first.

For every depth:
- The first node we encounter is the node visible
  from the right side.
- If result length == current depth, no node has been
  added for this level yet, so add the current node.

Traversal:
    Root → Right → Left

Why Right first?
Because we want the first node encountered at each
level to be the rightmost node.

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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def solve(node,depth):
            if node is None:
                return
            if depth==len(ans):
                ans.append(node.val)
            solve(node.right,depth+1)
            solve(node.left,depth+1)
        solve(root,0)
        return ans