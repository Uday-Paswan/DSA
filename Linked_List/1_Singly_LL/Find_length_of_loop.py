"""
Problem: Find Length of Loop
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/find-length-of-loop/1
Difficulty: Easy

Pattern:
- Linked List
- Fast & Slow Pointers (Floyd's Cycle Detection)

Approach:
Use slow and fast pointers to detect a cycle. If they meet,
keep one pointer fixed and move the other pointer one step at
a time until it reaches the meeting point again, counting the
number of steps. The count represents the length of the loop.
If no cycle exists, return 0.

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

def count_loop(head):
    slow=head
    fast=head
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            fast=fast.next
            count=1
            while slow!=fast:
                fast=fast.next
                count+=1
            return count 
    return 0
