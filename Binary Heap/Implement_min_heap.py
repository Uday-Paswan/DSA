"""
Problem: Implement Min Heap

Topic:
- Heap
- Binary Heap
- Priority Queue

Min Heap Property:
    Every parent node must be smaller than or equal to
    its children.

Example:

        2
       / \
      5   3
     / \
    8   7

Array representation:
[2, 5, 3, 8, 7]

Important:
    Smallest element is always at index 0.

Index formulas:
    Parent = (i - 1) // 2
    Left   = 2 * i + 1
    Right  = 2 * i + 2

Main Operations:
    Insert  → O(log n)
    Get Min → O(1)
    Extract Min → O(log n)
"""


class MinHeap:

    def __init__(self):

        # List used to store the heap
        self.heap = []


    # -----------------------------------------------------
    # INSERT
    # -----------------------------------------------------

    def insert(self, value):

        # Add the new value at the end of the heap
        self.heap.append(value)

        # Start from the newly inserted element
        i = len(self.heap) - 1

        # Move the element upward until the min heap
        # property is restored
        while i > 0:

            # Find the parent index
            parent = (i - 1) // 2

            # If parent is already smaller,
            # heap property is satisfied
            if self.heap[parent] <= self.heap[i]:
                break

            # Otherwise, swap parent and current element
            self.heap[parent], self.heap[i] = (
                self.heap[i],
                self.heap[parent]
            )

            # Move upward to the parent's position
            i = parent


    # -----------------------------------------------------
    # GET MINIMUM
    # -----------------------------------------------------

    def get_min(self):

        # In a min heap, the smallest element
        # is always at index 0
        if len(self.heap) == 0:
            return None

        return self.heap[0]


    # -----------------------------------------------------
    # EXTRACT MINIMUM
    # -----------------------------------------------------

    def extract_min(self):

        # If heap is empty, there is nothing to remove
        if len(self.heap) == 0:
            return None

        # If there is only one element,
        # remove and return it
        if len(self.heap) == 1:
            return self.heap.pop()

        # Store the minimum element
        minimum = self.heap[0]

        # Move the last element to the root
        self.heap[0] = self.heap.pop()

        # Start fixing the heap from the root
        i = 0

        while True:

            # Calculate indexes of children
            left = 2 * i + 1
            right = 2 * i + 2

            # Assume current node is the smallest
            smallest = i

            # Check if left child exists and is smaller
            if left < len(self.heap) and \
               self.heap[left] < self.heap[smallest]:

                smallest = left

            # Check if right child exists and is smaller
            if right < len(self.heap) and \
               self.heap[right] < self.heap[smallest]:

                smallest = right

            # If current node is already the smallest,
            # the heap property is restored
            if smallest == i:
                break

            # Swap current node with the smallest child
            self.heap[i], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[i]
            )

            # Continue fixing the subtree
            i = smallest

        return minimum
"""""
### Operations to remember

```text id="9flr0h"
INSERT
  ↓
Add at END
  ↓
Compare with parent
  ↓
If smaller → SWAP
  ↓
Move UP
```

```text id="g0y7aj"
EXTRACT MIN
  ↓
Remove ROOT
  ↓
Move LAST element to ROOT
  ↓
Compare with children
  ↓
Choose SMALLER child
  ↓
If child is smaller → SWAP
  ↓
Move DOWN
```

### Complexity

| Operation       |       Time |
| --------------- | ---------: |
| Insert          | `O(log n)` |
| Get Minimum     |     `O(1)` |
| Extract Minimum | `O(log n)` |

### Most important difference from Heapify

**Heapify** usually means fixing a node that is already inside the heap:

```text
Node violates heap property
        ↓
Heapify
        ↓
Move DOWN
```

**Insert** starts with a completely new element:

```text
New element
    ↓
Add at END
    ↓
Move UP
```

So remember:

```text
INSERT       → UP
EXTRACT MIN  → DOWN
HEAPIFY      → usually DOWN
```
"""