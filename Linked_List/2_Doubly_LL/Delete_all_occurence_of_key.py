"""
Problem: Delete All Occurrences of a Given Key in a Doubly Linked List
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list/1
Difficulty: Medium

Pattern:
- Doubly Linked List
- Pointer Manipulation

Approach:
Traverse the doubly linked list. Whenever a node with the given
key is found, update the previous node's next pointer and the
next node's prev pointer to bypass the current node. Handle the
special case where the node to be deleted is the head. Continue
traversing until the end of the list.

Time Complexity: O(n)
Space Complexity: O(1)
"""
"""
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

"""
#This is the GFG Solution
class Solution:
    
    # Function to delete all occurrences of x
    def deleteAllOccurOfX(self, head, x):
        # code here
        current=head
        while current!=None:
            new_node=current.next
            if current.data==x:
                if current.prev==None:
                    head=current.next
                    if head is not None:
                        head.prev=None 
                elif current.next==None:
                    current.prev.next=None
                else:
                    current.next.prev=current.prev
                    current.prev.next=current.next
            current=new_node
        return head

    