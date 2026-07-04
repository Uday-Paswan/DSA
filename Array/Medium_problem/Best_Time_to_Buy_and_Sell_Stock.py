"""
Problem: Best Time to Buy and Sell Stock
Platform: LeetCode
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Difficulty: Easy

Pattern:
- Array
- Greedy
- Prefix Minimum

Approach:
Maintain the minimum buying price while traversing the array.
Calculate the profit for each day and update the maximum profit.
Return the maximum profit after one pass.

Time Complexity: O(n)
Space Complexity: O(1)
"""
def maxProfit(prices):
        min_buy=prices[0]
        max_profit=0
        for i in range(0,len(prices)):
            min_buy=min(min_buy,prices[i])
            max_profit=max(max_profit,prices[i]-min_buy)
        return max_profit

#Test case 
prices=[7,1,5,3,6,4]
print(maxProfit(prices))