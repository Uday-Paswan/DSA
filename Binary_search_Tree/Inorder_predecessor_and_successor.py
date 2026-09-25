"""
Problem: Inorder Successor and Predecessor
Platform: GeeksforGeeks
Difficulty: Medium

Pattern:
- Binary Search Tree
- Inorder Successor
- Inorder Predecessor
- Iteration

Definitions:

Predecessor:
Largest value smaller than the key.

Successor:
Smallest value greater than the key.

BST Property:
    left < root < right

Approach:

Predecessor:
- If current.data < key:
      current can be a predecessor.
      Save it and move RIGHT to find a larger candidate.
- Otherwise:
      Move LEFT.

Successor:
- If current.data > key:
      current can be a successor.
      Save it and move LEFT to find a smaller candidate.
- Otherwise:
      Move RIGHT.

Time Complexity: O(h)
Space Complexity: O(1)

where h = height of the BST.
"""
class Solution:

    def findPreSuc(self, root, key):

        predecessor = None
        successor = None

        current = root

        while current:

            if current.data < key:
                predecessor = current
                current = current.right

            else:
                current = current.left

        current = root

        while current:

            if current.data > key:
                successor = current
                current = current.left

            else:
                current = current.right

        return [predecessor, successor]