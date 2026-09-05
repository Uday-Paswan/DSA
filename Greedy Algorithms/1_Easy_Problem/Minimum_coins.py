"""
Problem: Minimum Coins
Platform: GeeksforGeeks
Difficulty: Easy

Pattern:
- Greedy
- Sorting / Reverse Traversal

Approach:
Use the largest denomination first.

1. Start from the largest coin.
2. Keep taking the coin while it is less than or equal to
   the remaining amount.
3. Subtract the coin value from the remaining amount.
4. Move to the next smaller denomination.
5. Count the number of coins used.

For this problem, the denominations are:
[1, 2, 5, 10]

Time Complexity: O(n + number of coins used)
Space Complexity: O(1) auxiliary space
"""
def minimum_coins(N):
    coins=[1,2,5,10]
    n=len(coins)
    count=0
    remaining=N
    for i in range(n-1,-1,-1):
        while coins[i]<=remaining:
            count+=1
            remaining-=coins[i]
    return count

#Test case
N=39
print(minimum_coins(N))