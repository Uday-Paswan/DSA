# Build Heap from Given Array
'''
**Problem:** Build Heap from a Given Array
**Platform:** GeeksforGeeks
**Difficulty:** Medium
**Pattern:** Heap / Heapify / Binary Heap

### Approach

* We are given an unsorted array.
* Convert the array into a **Min Heap** using the `heapify` algorithm.
* Leaf nodes already satisfy the heap property, so we don't need to heapify them.
* Start from the **last non-leaf node**:

```text
last non-leaf = n//2 - 1
```

* Move from right to left and apply **min heapify** to every non-leaf node.
* After all nodes are heapified, the array becomes a Min Heap.

### Code

'''
class Solution:

    def minHeapify(self, arr, n, i):

        # Assume current node is the smallest
        smallest = i

        # Find left and right child
        left = 2 * i + 1
        right = 2 * i + 2

        # Check if left child is smaller
        if left < n and arr[left] < arr[smallest]:
            smallest = left

        # Check if right child is smaller
        if right < n and arr[right] < arr[smallest]:
            smallest = right

        # If a smaller child is found, swap
        if smallest != i:

            arr[i], arr[smallest] = arr[smallest], arr[i]

            # Heapify the affected subtree
            self.minHeapify(arr, n, smallest)


    def buildMinHeap(self, arr):

        n = len(arr)

        # Start from the last non-leaf node
        start = n // 2 - 1

        # Heapify every non-leaf node from bottom to top
        for i in range(start, -1, -1):
            self.minHeapify(arr, n, i)

        return arr
'''
### Example

Given:

```text
[5, 3, 8, 1, 2]
```

After building a Min Heap:

```text
[1, 2, 8, 5, 3]
```

Tree:

```text
        1
       / \
      2   8
     / \
    5   3
```

Every parent is smaller than its children.

### Why start from `n//2 - 1`?

Leaf nodes don't have children, so there is nothing to heapify.

For:

```text
n = 5
```

```text
n//2 - 1
= 5//2 - 1
= 1
```

So we start at index `1`:

```text
Index:  0   1   2   3   4
Array: [5,  3,  8,  1,  2]
            ↑
       last non-leaf
```

Then:

```text
1 → 0
```

So we heapify index `1`, then index `0`.

### Complexity

**Time:** `O(n)`
**Space:** `O(log n)` for recursive heapify.

### Key Point

```text
Unsorted Array
      ↓
Start from last non-leaf
      ↓
Heapify bottom → top
      ↓
Min Heap
```

**Memory Trick:**

```text
Build Heap → Start at n//2 - 1 → Move backwards → Heapify
'''
