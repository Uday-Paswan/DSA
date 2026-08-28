"""
Problem: Min Stack
Platform: LeetCode
Problem Number: 155
Difficulty: Medium

Pattern:
- Stack
- Auxiliary Stack
- Data Structure Design

Approach:
Use two stacks:

1. stack:
   Stores all the values normally.

2. minStack:
   Stores the minimum value at each position.

Whenever a new value is pushed:
- Push it into stack.
- Compare it with the current minimum.
- Push the smaller value into minStack.

Whenever a value is popped:
- Pop from both stack and minStack.

The top of minStack always contains the current minimum,
so getMin() can be performed in O(1) time.

Time Complexity:
- push()    → O(1)
- pop()     → O(1)
- top()     → O(1)
- getMin()  → O(1)

Space Complexity: O(n)
"""
class MinStack:

    def __init__(self):
        self.items=[]

    def push(self, value: int) -> None:
        if len(self.items)==0:
            self.items.append([value,value])
        else:
            mini=min(self.items[-1][1],value)
            self.items.append([value,mini])
        

    def pop(self) -> None:
        if len(self.items)==0:
            return -1
        x=self.items.pop()
        return x
        

    def top(self) -> int:
        return self.items[-1][0]
        

    def getMin(self) -> int:
        if len(self.items)==0:
            return 0
        return self.items[-1][1]
    