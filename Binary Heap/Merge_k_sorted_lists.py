"""
Problem: Merge k Sorted Lists
Platform: LeetCode
Link: https://leetcode.com/problems/merge-k-sorted-lists/
Difficulty: Hard

Pattern:
- Heap
- Priority Queue
- Linked List
- Min Heap

Approach:
Use a Min Heap to always get the smallest node among the k
sorted linked lists.

First, add the first node of every non-empty linked list
to the Min Heap.

Then repeatedly:
- Remove the smallest node from the heap.
- Add it to the result linked list.
- If that node has a next node, add the next node to the heap.

Since the heap always contains the smallest available node
from each list, the final linked list will be sorted.

Time Complexity: O(N log k)
Space Complexity: O(k)

Where:
N = total number of nodes across all linked lists
k = number of linked lists
"""

import heapq

class Solution:

    def mergeKLists(self, lists: list[list]):

        # Min Heap
        heap = []

        # Add the first node of every linked list
        # to the heap.
        for i, node in enumerate(lists):

            # Ignore empty linked lists
            if node:

                # Store:
                # node.val → value used for comparison
                # i         → unique value to avoid comparing nodes
                # node      → actual linked list node
                heapq.heappush(heap, (node.val, i, node))

        # Dummy node helps us easily build the result list
        dummy = ListNode(0)

        # Pointer used to build the merged list
        current = dummy

        # Continue until the heap becomes empty
        while heap:

            # Get the smallest node from the heap
            value, i, node = heapq.heappop(heap)

            # Add this node to the result list
            current.next = node

            # Move current pointer forward
            current = current.next

            # If the current node has another node,
            # add that next node to the heap.
            if node.next:

                heapq.heappush(
                    heap,
                    (node.next.val, i, node.next)
                )

        # dummy itself is not part of the answer,
        # so return the node after dummy.
        return dummy.next