"""
Problem: Binary Tree Maximum Path Sum
Platform: LeetCode
Problem Number: 124
Difficulty: Hard

Pattern:
- Binary Tree
- DFS
- Recursion
- Postorder Traversal
- Tree DP

Approach:
For every node, calculate the maximum path sum that can be
extended to its parent.

1. Recursively calculate the best contribution from the left subtree.
2. Recursively calculate the best contribution from the right subtree.
3. If a subtree gives a negative contribution, ignore it by
   replacing it with 0.
4. Calculate the path passing through the current node:

       leftsum + node.val + rightsum

5. Update the global maximum.
6. Return only one side to the parent:

       node.val + max(leftsum, rightsum)

Why only one side is returned?
A path going from the current node to its parent can continue
through only one child. Using both sides would create a fork.

Time Complexity: O(n)
Space Complexity: O(h)
where h = height of the tree because of recursion stack.
"""
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        maxi = float("-inf")

        def solve(node):
            nonlocal maxi

            if node is None:
                return 0

            leftsum = solve(node.left)
            rightsum = solve(node.right)

            leftsum = max(0, leftsum)
            rightsum = max(0, rightsum)

            maxi = max(
                maxi,
                leftsum + node.val + rightsum
            )

            return node.val + max(leftsum, rightsum)

        solve(root)

        return maxi