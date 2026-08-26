"""
Problem: Implement Queue Using Array
Platform: GeeksforGeeks
Difficulty: Easy

Pattern:
- Queue
- Array
- FIFO (First In, First Out)

Approach:
Implement a queue using an array (Python list).

Operations:
1. enqueue(x)  -> Insert x at the rear.
2. dequeue()   -> Remove and return the front element.
3. getFront()  -> Return the front element.
4. getRear()   -> Return the rear element.
5. isEmpty()   -> Check whether the queue is empty.
6. isFull()    -> Check whether the queue has reached its capacity.

The queue follows FIFO:
First In → First Out

Time Complexity:
- enqueue()  → O(1)
- dequeue()  → O(n) using list.pop(0)
- getFront() → O(1)
- getRear()  → O(1)
- isEmpty()  → O(1)
- isFull()   → O(1)

Space Complexity: O(n)
"""
class myQueue:
    def __init__(self, n):
        self.items = []
        self.n = n

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return len(self.items) == self.n

    def enqueue(self, x):
        if not self.isFull():
            self.items.append(x)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return -1

    def getFront(self):
        if not self.isEmpty():
            return self.items[0]
        return -1

    def getRear(self):
        if not self.isEmpty():
            return self.items[-1]
        return -1