"""
Problem: Kth Largest Element in an Array
Platform: LeetCode
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
Difficulty: Medium

Pattern:
- Heap
- Priority Queue
- Min Heap

Approach:
Use a Min Heap of size k.

Traverse through the array and push each element into the heap.
If the heap size becomes greater than k, remove the smallest element.

This keeps only the k largest elements in the heap.
The smallest element among these k elements is the kth largest
element in the entire array.

Therefore, heap[0] gives the kth largest element.

Time Complexity: O(n log k)
Space Complexity: O(k)
"""

import heapq

import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        ans=[]
        for num in nums:
            heapq.heappush(ans,num)
            if len(ans)>k:
                heapq.heappop(ans)
        return ans[0]