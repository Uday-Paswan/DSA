"""
Problem: Linked List Cycle II
Platform: LeetCode
Link: https://leetcode.com/problems/linked-list-cycle-ii/
Difficulty: Medium

Pattern:
- Linked List
- Fast & Slow Pointers (Floyd's Cycle Detection)

Approach:
Use Floyd's Cycle Detection algorithm. First, detect whether a
cycle exists using slow and fast pointers. If they meet, move one
pointer back to the head while keeping the other at the meeting
point. Move both pointers one step at a time. The node where they
meet again is the starting node of the cycle.

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

def detect_cycel(head):
    slow=head
    fast=head
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            slow=head
            while slow!=fast:
                slow=slow.next
                fast=fast.next
            return slow
    return None

#Test case
# TO test the cycle we need to write another code which make cycle.
# IN leetcode this cases is handle automatically but here we need to write everything to test the case.