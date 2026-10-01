"""
Topic: Heapify Algorithm
Pattern: Binary Heap / Heap / Priority Queue

Heapify:
Heapify is used to maintain the heap property of a binary heap.

Min Heap:
    Parent <= Children
    Smallest element stays at the root.

Max Heap:
    Parent >= Children
    Largest element stays at the root.

For a node at index i:
    Left child  = 2*i + 1
    Right child = 2*i + 2

Time Complexity: O(log n) for heapifying one node
Space Complexity: O(log n) for recursive implementation
"""


# ---------------------------------------------------------
# MIN HEAPIFY
# ---------------------------------------------------------

def min_heapify(arr, n, i):

    # Assume the current node is the smallest
    smallest = i

    # Calculate the indexes of left and right children
    left = 2 * i + 1
    right = 2 * i + 2

    # If left child exists and is smaller than current smallest
    if left < n and arr[left] < arr[smallest]:
        smallest = left

    # If right child exists and is smaller than current smallest
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    # If the smallest element is not the current node,
    # swap the current node with the smallest child
    if smallest != i:

        arr[i], arr[smallest] = arr[smallest], arr[i]

        # After swapping, the element moved down.
        # Heapify that subtree again to restore the heap property.
        min_heapify(arr, n, smallest)


# ---------------------------------------------------------
# MAX HEAPIFY
# ---------------------------------------------------------

def max_heapify(arr, n, i):

    # Assume the current node is the largest
    largest = i

    # Calculate the indexes of left and right children
    left = 2 * i + 1
    right = 2 * i + 2

    # If left child exists and is greater than current largest
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest element is not the current node,
    # swap the current node with the largest child
    if largest != i:

        arr[i], arr[largest] = arr[largest], arr[i]

        # After swapping, the element moved down.
        # Heapify that subtree again to restore the heap property.
        max_heapify(arr, n, largest)

## Key Idea

# ```text
# MIN HEAPIFY
#     ↓
# Find smallest among:
# Parent + Left + Right
#     ↓
# Swap with smallest
#     ↓
# Continue downward


# MAX HEAPIFY
#     ↓
# Find largest among:
# Parent + Left + Right
#     ↓
# Swap with largest
#     ↓
# Continue downward
# ```

# ## Important Point

# `heapify()` does **not automatically mean both min heap and max heap**.

# It is the general process of fixing a heap.

# ```text
# Heapify
#    |
#    ├── Min Heapify → choose SMALLER
#    |
#    └── Max Heapify → choose LARGER
# ```

# ## Example

# For:

# ```python
# arr = [5, 3, 8]
# ```

# ### Min Heapify

# ```text
#         5
#        / \
#       3   8

# Choose 3 → swap

#         3
#        / \
#       5   8
# ```

# Result:[3, 5, 8]
# ```

# ### Max Heapify

# ```text
#         5
#        / \
#       3   8

# Choose 8 → swap

#         8
#        / \
#       3   5
# ```

# Result:[8, 3, 5]
# ```

# Memory Trick
# MIN → Minimum should come to the top
#       → choose SMALLER child

# MAX → Maximum should come to the top
#       → choose LARGER child
