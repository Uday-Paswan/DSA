"""
Problem: Maximum Points You Can Obtain from Cards
Platform: LeetCode
Problem Number: 1423
Difficulty: Medium

Pattern:
- Sliding Window
- Two Pointers
- Array

Approach:
We need to choose exactly k cards from either the beginning
or the end of the array.

Start by taking all k cards from the left.

Then gradually:
1. Remove one card from the left.
2. Add one card from the right.
3. Calculate the new total.
4. Keep track of the maximum score.

This checks all possible combinations of:
- k cards from left, 0 from right
- k-1 cards from left, 1 from right
- k-2 cards from left, 2 from right
- ...
- 0 cards from left, k from right

Time Complexity: O(k)
Space Complexity: O(1)
"""
def maximum_points(cardPoints,k):
    n=len(cardPoints)
    if n==k:
        return sum(cardPoints)
    left_sum=0
    right_sum=0
    for i in range(0,k):
        left_sum+=cardPoints[i]
    maxi=left_sum
    right_index=n-1
    for i in range(k-1,-1,-1):
        left_sum-=cardPoints[i]
        right_sum+=cardPoints[right_index]
        maxi=max(maxi,left_sum+right_sum)
        right_index-=1
    return maxi

#Test Case
cardPoints = [9,7,7,9,7,7,9]
k = 7
print(maximum_points(cardPoints,k))