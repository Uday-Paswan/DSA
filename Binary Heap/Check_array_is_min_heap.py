"""
Problem: Check if Array is a Min Heap

Topic:
- Heap
- Binary Heap

Min Heap Property:
    Every parent must be smaller than or equal to
    its children.

Example of Min Heap:

        1
       / \
      3   2
     / \
    5   4

Array:
[1, 3, 2, 5, 4]

Index formulas:
    Left child  = 2*i + 1
    Right child = 2*i + 2

Approach:
    Check every parent node.
    If any child is smaller than its parent,
    the array is NOT a min heap.

Time Complexity: O(n)
Space Complexity: O(1)
"""


def is_min_heap(arr):

    n = len(arr)

    # Check every node that can have children
    # Leaf nodes do not need to be checked.
    for i in range(n // 2):

        # Index of left child
        left = 2 * i + 1

        # Index of right child
        right = 2 * i + 2

        # Check left child
        if left < n and arr[i] > arr[left]:
            return False

        # Check right child
        if right < n and arr[i] > arr[right]:
            return False

    # If no parent violates the min heap property
    return True

### Example
arr = [1, 3, 2, 5, 4]

print(is_min_heap(arr))