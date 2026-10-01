# Convert Min Heap to Max Heap
"""
**Problem:** Convert Min Heap to Max Heap
**Platform:** GeeksforGeeks
**Difficulty:** Easy
**Pattern:** Heap / Heapify / Binary Heap

### Approach

* We are given an array that represents a **Min Heap**.
* We need to convert it into a **Max Heap**.
* We can use the same **Build Heap** approach.
* The only difference is that instead of `minHeapify()`, we use **maxHeapify()**.
* Start from the **last non-leaf node**:

```text
n // 2 - 1
```

* Move from right to left and apply `maxHeapify()` to every non-leaf node.
"""
### Code
class Solution:

    # Fix the Max Heap property of the subtree
    # whose root is at index i.
    def maxHeapify(self, arr, n, i):

        # Initially assume that the current node
        # is the largest element.
        largest = i

        # Find the index of the left child.
        left = 2 * i + 1

        # Find the index of the right child.
        right = 2 * i + 2

        # Check if the left child exists and is
        # greater than the current largest element.
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check if the right child exists and is
        # greater than the current largest element.
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If the largest element is not the current node,
        # swap the current node with the largest child.
        if largest != i:

            arr[i], arr[largest] = arr[largest], arr[i]

            # The element moved down after swapping.
            # Heapify the affected subtree again.
            self.maxHeapify(arr, n, largest)


    # Convert the Min Heap into a Max Heap.
    def convertMinToMaxHeap(self, arr):

        # Store the size of the array.
        n = len(arr)

        # The last non-leaf node is at:
        # n//2 - 1
        start = n // 2 - 1

        # Start from the last non-leaf node
        # and move towards the root.
        for i in range(start, -1, -1):

            # Apply Max Heapify to the subtree
            # rooted at index i.
            self.maxHeapify(arr, n, i)

        # The array is now a Max Heap.
        return arr