"""
Problem: Diameter of Binary Tree
Platform: LeetCode
Problem Number: 543
Difficulty: Easy

Pattern:
- Binary Tree
- DFS
- Recursion
- Height of Binary Tree

Approach:
For every node, calculate the height of its left and right subtrees.

The diameter passing through the current node is:

    left_height + right_height

Keep track of the maximum diameter found.

Then return the height of the current subtree to the parent:

    1 + max(left_height, right_height)

Important:
Diameter is measured in NUMBER OF EDGES, not nodes.

Time Complexity: O(n)
Space Complexity: O(h)
where h = height of the tree because of recursion.
"""
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = 0

        def solve(node):
            nonlocal diameter

            if node is None:
                return 0

            left_height = solve(node.left)
            right_height = solve(node.right)

            diameter = max(
                diameter,
                left_height + right_height
            )

            return 1 + max(left_height, right_height)

        solve(root)

        return diameter