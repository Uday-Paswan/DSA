"""
Problem: Reverse Linked List
Platform: LeetCode
Link: https://leetcode.com/problems/reverse-linked-list/
Difficulty: Easy

Pattern:
- Linked List
- Pointer Manipulation
- Iterative

Approach:
Use three pointers: prev, current, and next_node.
Traverse the linked list while reversing the direction of each
node's next pointer. Move all three pointers forward until the
entire list is reversed. Finally, return the new head (prev).

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

def print_linked_list(head):
    current=head
    while current!=None:
        print(current.data,end="->")
        current=current.next
    print("None")

def reverse(head):
    current=head
    prev=None
    while current!=None:
        next_node=current.next
        current.next=prev
        prev=current
        current=next_node
    return prev

    

# Test Case
nums = [1, 2, 3, 4, 5]

head = create_linked_list(nums)

answer = reverse(head)

print_linked_list(answer)