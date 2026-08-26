"""
Problem: Implement Stack Using Array
Platform: GeeksforGeeks
Difficulty: Easy

Pattern:
- Stack
- Array
- LIFO (Last In, First Out)

Approach:
Implement a stack using an array (Python list).

Operations:
1. push(x)  -> Insert x at the top.
2. pop()    -> Remove and return the top element.
3. peek()   -> Return the top element without removing it.
4. isEmpty() -> Check whether the stack is empty.
5. isFull()  -> Check whether the stack has reached its capacity.

The stack follows LIFO:
Last In → First Out

Time Complexity:
- push()     → O(1)
- pop()      → O(1)
- peek()     → O(1)
- isEmpty()  → O(1)
- isFull()   → O(1)

Space Complexity: O(n)
"""
class myStack:
    def __init__(self, n):
        self.items = []
        self.n = n

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return len(self.items) == self.n

    def push(self, x):
        if not self.isFull():
            self.items.append(x)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return -1

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return -1
