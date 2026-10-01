"""
Problem: Kth Largest Element in a Stream
Platform: LeetCode
Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/
Difficulty: Easy

Pattern:
- Heap
- Priority Queue
- Min Heap

Approach:
Maintain a Min Heap containing only the k largest elements.

During initialization, add all elements from nums to the heap.
If the heap size becomes greater than k, remove the smallest element.

For every new value added through add(), push it into the heap.
If the heap size becomes greater than k, remove the smallest element.

The root of the Min Heap is always the kth largest element.

Time Complexity:
- Initialization: O(n log k)
- add(): O(log k)

Space Complexity: O(k)
"""

import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):

        # Store k because we need to maintain
        # only the k largest elements
        self.k = k

        # Create a Min Heap
        self.heap = []

        # Add all initial elements
        for num in nums:

            # Add current element to the heap
            heapq.heappush(self.heap, num)

            # If heap contains more than k elements,
            # remove the smallest element
            if len(self.heap) > k:
                heapq.heappop(self.heap)


    def add(self, val: int) -> int:

        # Add the new value to the Min Heap
        heapq.heappush(self.heap, val)

        # Keep only the k largest elements
        if len(self.heap) > self.k:

            # Remove the smallest element
            heapq.heappop(self.heap)

        # The smallest element among the k largest
        # elements is the kth largest element
        return self.heap[0]