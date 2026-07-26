"""
Problem: Remove Duplicates from a Sorted Doubly Linked List
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/remove-duplicates-from-a-sorted-doubly-linked-list/1
Difficulty: Easy

Pattern:
- Doubly Linked List
- Pointer Manipulation

Approach:
Traverse the sorted doubly linked list using a current pointer.
If the current node and the next node have the same value,
remove the duplicate node by updating both the next and prev
pointers. Otherwise, move the current pointer forward.
Continue until the end of the list and return the head.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# class Node:
#     def __init__(self, value):
#         self.data = value  # value stored in node
#         self.next = None
#         self.prev = None

#This is the GFG problem

class Solution:
    def removeDuplicates(self, headRef):
        # code here
        current=headRef
        while current is not None and current.next is not None:
            temp=current.next
            if current.data==temp.data:
                current.next=temp.next
                if temp.next is not None:
                    temp.next.prev=current
            else:
                current=current.next
        return headRef
               
           