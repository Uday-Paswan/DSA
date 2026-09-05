"""
Problem: Fractional Knapsack
Platform: GeeksforGeeks
Difficulty: Medium

Pattern:
- Greedy
- Sorting
- Fractional Knapsack

Approach:
For each item, calculate its value/weight ratio.

1. Create a list containing:
   - ratio
   - value
   - weight

2. Sort the items by ratio in descending order.

3. Start taking items from the highest ratio:
   - If the complete item fits, take it completely.
   - Otherwise, take only the fraction that fits.

4. Once the bag is full, stop.

Why Greedy?
An item with a higher value per unit weight gives more profit
for every unit of capacity, so we should take it first.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""
def knapsack(val,wt,capacity):
    items=[]
    for i in range(len(val)):
        ratio=val[i]/wt[i]
        items.append((ratio,val[i],wt[i]))
    items.sort(reverse=True)
    current_weight=0
    profit=0
    for ratio,value,weight in items:
        if current_weight+weight<=capacity:
            current_weight+=weight
            profit+=value
        else:
            remain=capacity-current_weight
            profit+=ratio*remain
            break
    return profit

#Test case
val= [60, 100, 120]
wt = [10, 20, 30]
capacity = 50

print(knapsack(val,wt,capacity))

    