"""
Problem: Find Pairs with Given Sum in Doubly Linked List
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1
Difficulty: Medium

Pattern:
- Doubly Linked List
- Two Pointers

Approach:
Initialize two pointers: left at the head and right at the tail
of the doubly linked list. Compare the sum of their values with
the target. If the sum is equal, store the pair and move both
pointers inward. If the sum is smaller, move the left pointer
forward. If the sum is larger, move the right pointer backward.
Continue until the pointers meet or cross.

Time Complexity: O(n)
Space Complexity: O(1)   (excluding the output list)
"""

# Structure of Doubly Linked List Node
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''
#This is the GFG solution

class Solution:
    def givenSumPairs(self, head, target):
        # code here
        left=head
        right=head
        result=[]
        while right.next!=None:
            right=right.next
        
        while left!=right and left!=right.next:
            current_sum=left.data+right.data
            if current_sum==target:
                result.append([left.data,right.data])
                left=left.next
                right=right.prev
            elif current_sum<target:
                left=left.next
            else:
                right=right.prev
        return result