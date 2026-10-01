# Heap Sort Algorithm
'''
**Problem:** Heap Sort Algorithm
**Platform:** GeeksforGeeks
**Difficulty:** Medium
**Pattern:** Heap / Sorting / Max Heap

### Approach

* Heap Sort uses a **Max Heap** to sort the array in ascending order.
* First, convert the array into a **Max Heap**.
* The largest element will be at index `0`.
* Swap the root (largest element) with the last element.
* Reduce the heap size because the last element is now in its correct position.
* Apply `maxHeapify()` to restore the Max Heap.
* Repeat until the entire array is sorted.
'''

### Code
class Solution:

    # Fix the Max Heap property of the subtree
    # whose root is at index i.
    def maxHeapify(self, arr, n, i):

        # Initially assume that the current node
        # is the largest element.
        largest = i

        # Find the left child.
        left = 2 * i + 1

        # Find the right child.
        right = 2 * i + 2

        # Check if the left child exists and is
        # greater than the current largest element.
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check if the right child exists and is
        # greater than the current largest element.
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If a child is larger than the current node,
        # swap them.
        if largest != i:

            arr[i], arr[largest] = arr[largest], arr[i]

            # The element moved down after swapping.
            # Heapify the affected subtree again.
            self.maxHeapify(arr, n, largest)


    # Heap Sort function.
    def heapSort(self, arr):

        # Store the size of the array.
        n = len(arr)

        # -------------------------------------------------
        # STEP 1: Build a Max Heap
        # -------------------------------------------------

        # Start from the last non-leaf node.
        start = n // 2 - 1

        # Heapify all non-leaf nodes from bottom to top.
        for i in range(start, -1, -1):

            self.maxHeapify(arr, n, i)


        # -------------------------------------------------
        # STEP 2: Extract the maximum element one by one
        # -------------------------------------------------

        # The root contains the largest element.
        # Move it to the end of the array.
        for i in range(n - 1, 0, -1):

            # Swap the root (largest) with the last
            # element of the current heap.
            arr[0], arr[i] = arr[i], arr[0]

            # The element at index i is now sorted.
            # So reduce the heap size to i.
            heap_size = i

            # Restore the Max Heap property.
            self.maxHeapify(arr, heap_size, 0)

        return arr

# For ascending order → Max Heap
# For descending order → Min Heap
