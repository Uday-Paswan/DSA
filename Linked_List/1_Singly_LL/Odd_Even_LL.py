"""
Problem: Odd Even Linked List
Platform: LeetCode
Link: https://leetcode.com/problems/odd-even-linked-list/
Difficulty: Medium

Pattern:
- Linked List
- Pointer Manipulation

Approach:
Maintain two pointers: odd and even. Connect all odd-indexed
nodes together and all even-indexed nodes together while
preserving their relative order. Finally, connect the end of
the odd list to the head of the even list.

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

#Main algorithm

def odd_even(head):
    if head is None or head.next is None:
        return head
    odd=head
    even=head.next
    even_head=even
    while even!=None and even.next!=None:
        odd.next=odd.next.next
        odd=odd.next
        even.next=even.next.next
        even=even.next
    odd.next=even_head
    return head