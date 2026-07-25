"""
Problem: Reverse a Doubly Linked List
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1
Difficulty: Easy

Pattern:
- Doubly Linked List
- Pointer Manipulation

Approach:
Traverse the doubly linked list and swap the next and prev
pointers of every node. After processing all nodes, update the
head to the last processed node, which becomes the new head of
the reversed list.

Time Complexity: O(n)
Space Complexity: O(1)
"""

#This is only the algorithm for reverse the DLL

class Solution:
    def reverse(self, head):
        current=head
        last=None
        while current is not None:
            last=current
            temp=current.prev
            current.prev=current.next
            current.next=temp
            current=current.prev
        head=last
        return head
        