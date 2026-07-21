"""
Problem: Middle of the Linked List
Platform: LeetCode
Link: https://leetcode.com/problems/middle-of-the-linked-list/
Difficulty: Easy

Pattern:
- Linked List
- Fast & Slow Pointers

Approach:
Use two pointers: slow and fast. Move the slow pointer one step
at a time and the fast pointer two steps at a time. When the fast
pointer reaches the end of the list, the slow pointer will be at
the middle node.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_linked_list(nums):
    if not nums:
        return None

    head = Node(nums[0])
    current = head

    for value in nums[1:]:
        current.next = Node(value)
        current = current.next

    return head


def middle(head):
    slow=head
    fast=head
    while fast!=None and fast.next!=None:
        slow=slow.next
        fast=fast.next.next
    return slow

#Test case
nums = [1,2,3,4,5]
head=create_linked_list(nums)
print(middle(head))