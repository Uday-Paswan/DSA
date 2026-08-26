"""
Problem: Implement Stack Using Queues
Platform: LeetCode
Problem Number: 225
Difficulty: Easy

Pattern:
- Stack
- Queue
- Data Structure Design
- FIFO → LIFO

Goal:
Implement a stack using only queue operations.

Stack follows:
LIFO (Last In, First Out)

Queue follows:
FIFO (First In, First Out)

Approach:
Use a queue to simulate stack behavior.

After adding a new element to the queue, move all previous
elements behind it. This makes the newest element stay at
the front of the queue.

Therefore:
- push(x)  -> Add x, then rotate previous elements.
- pop()    -> Remove from the front.
- top()    -> Return the front element.
- empty()  -> Check whether the queue is empty.

Time Complexity:
- push()  → O(n)
- pop()   → O(1)
- top()   → O(1)
- empty() → O(1)

Space Complexity: O(n)
"""
from collections import deque


class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0
