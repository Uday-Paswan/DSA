"""
Problem: Hand of Straights
Platform: LeetCode
Link: https://leetcode.com/problems/hand-of-straights/
Difficulty: Medium

Pattern:
- Greedy
- Hashing / Frequency Counting
- Min Heap

Approach:
First, check whether the number of cards is divisible by
groupSize. If not, forming consecutive groups is impossible.

Count the frequency of each card using Counter.
Put the distinct card values into a min heap so the smallest
remaining card is processed first.

Take the smallest card as the starting point of a group.
Check whether every consecutive card from first to
first + groupSize - 1 is available.

Decrease the frequency of each card used.
When a card's frequency becomes zero, it must be the smallest
remaining card in the heap. Otherwise, a smaller card would
be left unused, so return False.

Remove exhausted cards from the heap and continue until
all cards have been grouped.

Time Complexity: O(N log K), where K is the number of
distinct card values.
Space Complexity: O(K)
"""

import heapq
from collections import Counter


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:

        # The total number of cards must be divisible by groupSize.
        if len(hand) % groupSize != 0:
            return False

        # Count the frequency of each card value.
        count = Counter(hand)

        # Create a min heap containing distinct card values.
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        # Process cards until no values remain.
        while min_heap:

            # The smallest remaining card starts the next group.
            first = min_heap[0]

            # Check for all consecutive cards in this group.
            for i in range(first, first + groupSize):

                # If a required card does not exist, grouping fails.
                if i not in count:
                    return False

                # Use one copy of the current card.
                count[i] -= 1

                # If all copies are used, remove the card from the heap.
                if count[i] == 0:

                    # The exhausted card must be the heap minimum.
                    if i != min_heap[0]:
                        return False

                    # Remove the exhausted card.
                    heapq.heappop(min_heap)

        # Every card was successfully placed into a consecutive group.
        return True
