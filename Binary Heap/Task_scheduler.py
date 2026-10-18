"""
Problem: Task Scheduler
Platform: LeetCode
Link: https://leetcode.com/problems/task-scheduler/
Difficulty: Medium

Pattern:
- Greedy
- Hashing / Frequency Counting
- Max Heap
- Queue (Cooldown)

Approach:
Count the frequency of each task using Counter.
Store the negative frequencies in a max heap to process
the most frequent task first.

Use a cooldown queue to track tasks that have remaining
executions and the time when they become available again.

At each time unit:
1. Execute the most frequent available task, if one exists.
2. Decrease its frequency and add it to the cooldown queue
   if more executions remain.
3. Return tasks to the heap when their cooldown expires.
4. If no task is available, the time unit becomes idle.

Continue until both the heap and cooldown queue are empty.

Time Complexity: O(T * log K), where T includes idle intervals
and K is the number of distinct task types.
Space Complexity: O(K)
"""

import heapq
from collections import Counter, deque


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:

        # Count the frequency of each task.
        count = Counter(tasks)

        # Store negative frequencies to simulate a max heap.
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        # Track the current time.
        time = 0

        # Store [remaining frequency, cooldown completion time].
        cooldown = deque()

        # Continue while tasks remain available or in cooldown.
        while max_heap or cooldown:
            time += 1

            # Execute the task with the highest remaining frequency.
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)

                # Add the task to cooldown if executions remain.
                if cnt != 0:
                    cooldown.append([cnt, time + n])

            # Return the task to the heap once its cooldown expires.
            if cooldown and cooldown[0][1] <= time:
                heapq.heappush(max_heap, cooldown.popleft()[0])

        # Return the total time, including idle intervals.
        return time
