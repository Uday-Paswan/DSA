"""
Problem: Valid Parentheses
Platform: LeetCode
Problem Number: 20
Difficulty: Easy

Pattern:
- Stack
- String
- Parentheses Matching

Approach:
Use a stack to store opening brackets.

For every character:
1. If it is an opening bracket, push it into the stack.
2. If it is a closing bracket:
   - Check whether the stack is empty.
   - Pop the most recent opening bracket.
   - Check whether it matches the closing bracket.
3. If the brackets do not match, return False.

After processing the entire string, the stack must be empty
for the parentheses to be valid.

Time Complexity: O(n)
Space Complexity: O(n)
"""
def is_valid(s):
    stack=[]
    for bracket in s:
        if bracket=="(" or bracket=="[" or bracket=="{":
            stack.append(bracket)
        else:
            if len(stack)==0:
                return False
            ch=stack.pop()
            if ((bracket=="]" and ch=="[")
                or (bracket==")" and ch=="(")
                or (bracket=="}" and ch=="{")
                ):
                continue
            else:
                return False
    return len(stack)==0

#Test Case
s = "([)]"
print(is_valid(s))
