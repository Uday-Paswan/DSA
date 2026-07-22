"""
Problem: Linked List Cycle
Platform: LeetCode
Link: https://leetcode.com/problems/linked-list-cycle/
Difficulty: Easy

Pattern:
- Linked List
- Fast & Slow Pointers (Floyd's Cycle Detection)

Approach:
Use two pointers: slow and fast. Move slow one step at a time
and fast two steps at a time. If the linked list contains a cycle,
both pointers will eventually meet. If fast or fast.next becomes
None, then no cycle exists.

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
            return True 
    return False

#Test Case
nums = [1, 2, 3, 4, 5]

head = create_linked_list(nums)
print(detect_cycel(head))