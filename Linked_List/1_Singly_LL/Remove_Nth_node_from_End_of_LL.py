"""
Problem: Remove Nth Node From End of List
Platform: LeetCode
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Difficulty: Medium

Pattern:
- Linked List
- Fast & Slow Pointers
- Dummy Node

Approach:
Create a dummy node pointing to the head. Move the fast pointer
n steps ahead. Then move both slow and fast pointers together
until fast reaches the last node. The slow pointer will be just
before the node to be deleted. Update slow.next to skip the
target node and return dummy.next.

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def create_linked_list(nums):
    if not nums:
        return None
    head=Node(nums[0])
    current=head
    for i in range(1,len(nums)):
        new_node=Node(nums[i])
        current.next=new_node
        current=current.next
    return head

#ONlY ALGRORITHM 

def remove(head,n):
    dummy=Node(0)
    dummy.next=head
    slow=dummy
    fast=dummy
    for _ in range(n):
        fast=fast.next
    while fast.next!=None:
        slow=slow.next
        fast=fast.next
    slow.next=slow.next.next
    return dummy.next 
