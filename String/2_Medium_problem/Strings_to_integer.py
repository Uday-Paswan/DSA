"""
Problem: String to Integer (atoi)
Platform: LeetCode
Link: https://leetcode.com/problems/string-to-integer-atoi/
Difficulty: Medium

Pattern:
- String
- Simulation

Approach:
Skip leading whitespaces, determine the sign, and parse the
digits one by one. Stop when a non-digit character is found.
Clamp the result within the 32-bit signed integer range before
returning the final value.

Time Complexity: O(n)
Space Complexity: O(1)
"""
def atoi(s):
    i=0
    while i<len(s) and s[i]==" ":
        i+=1
    sign=1
    if i<len(s) and s[i]=="-":
        sign=-1
        i+=1
    elif i<len(s) and s[i]=="+":
        i+=1
     
    num=0
    while i<len(s) and s[i].isdigit():
        digit=int(s[i])
        num=num*10+digit
        i+=1

    num=sign*num

    if num>2**31-1:
        return 2**31-1
    elif num<-2**31:
        return -2**31
    
    return num

#Test case
s = "1337c0d3"
print(atoi(s))
