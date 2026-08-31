"""
Problem: Asteroid Collision
Platform: LeetCode
Problem Number: 735
Difficulty: Medium

Pattern:
- Stack
- Simulation

Approach:
Use a stack to simulate asteroid collisions.

Rules:
- Positive asteroid → Moving right.
- Negative asteroid → Moving left.
- Collision happens only when:
  stack top is positive and current asteroid is negative.

For every asteroid:
1. Push it if no collision is possible.
2. While collision is possible:
   - Smaller asteroid explodes.
   - Equal size → Both explode.
   - Larger asteroid survives.
3. Add the surviving asteroid to the stack.

Time Complexity: O(n)
Space Complexity: O(n)
"""
def collisions(asteroids):
    stack=[]
    for i in range(len(asteroids)):
        if asteroids[i]>0:
            stack.append(asteroids[i])
        else:
            while len(stack)!=0 and stack[-1]>0 and stack[-1]<abs(asteroids[i]):
                stack.pop()
            if len(stack)!=0 and stack[-1]==abs(asteroids[i]):
                stack.pop()
            elif len(stack)==0 or stack[-1]<0:
                stack.append(asteroids[i])
    return stack

#Test case
asteroids = [5,10,-5]
print(collisions(asteroids))