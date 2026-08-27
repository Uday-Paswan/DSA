"""
Problem: Implement Queue using Stacks
Platform: LeetCode
Problem Number: 232
Difficulty: Easy

Pattern:
- Stack
- Queue
- Data Structure Design
- FIFO using LIFO

Goal:
Implement a queue using two stacks.

Queue follows:
FIFO (First In, First Out)

Stack follows:
LIFO (Last In, First Out)

Approach:
Use two stacks: st1 and st2.

For push():
1. Move all elements from st1 to st2.
2. Add the new element to st1.
3. Move all elements back from st2 to st1.

This keeps the oldest element at the top of st1.

For pop():
Remove the top element from st1.

For peek():
Return the top element of st1 without removing it.

For empty():
Check whether st1 is empty.

Time Complexity:
- push()  → O(n)
- pop()   → O(1)
- peek()  → O(1)
- empty() → O(1)

Space Complexity: O(n)
"""

class MyQueue:

    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, x: int) -> None:

        while self.st1:
            self.st2.append(self.st1.pop())

        self.st1.append(x)

        while self.st2:
            self.st1.append(self.st2.pop())

    def pop(self) -> int:

        if not self.st1:
            return -1

        return self.st1.pop()

    def peek(self) -> int:

        if not self.st1:
            return -1

        return self.st1[-1]

    def empty(self) -> bool:

        return not self.st1