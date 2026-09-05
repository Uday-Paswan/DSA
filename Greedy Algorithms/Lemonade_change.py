"""
Problem: Lemonade Change
Platform: LeetCode
Problem Number: 860
Difficulty: Easy

Pattern:
- Greedy
- Simulation

Approach:
Each lemonade costs $5.

We maintain the number of:
- $5 bills
- $10 bills

For each customer:

1. If the customer gives $5:
   - Keep the $5 bill.

2. If the customer gives $10:
   - Give one $5 as change.
   - If no $5 is available, return False.

3. If the customer gives $20:
   - Prefer giving one $10 + one $5 as change.
   - Otherwise, give three $5 bills.
   - If neither is possible, return False.

Why Greedy?
For a $20 bill, prefer $10 + $5 over three $5 bills
because $5 bills are more useful for future $10 customers.

Time Complexity: O(n)
Space Complexity: O(1)
"""
def lemonade_change(bills):
    n=len(bills)
    five=0
    ten=0
    for i in range(n):
        if bills[i]==5:
            five+=1
        elif bills[i]==10:
            if five>=1:
                five-=1
                ten+=1
            else:
                return False
        else:
            if ten>=1 and five>=1:
                ten-=1
                five-=1
            elif five>=3:
                five-=3
            else:
                return False
    return True

#Test Case
bills = [5,5,10,10,20]
print(lemonade_change(bills))