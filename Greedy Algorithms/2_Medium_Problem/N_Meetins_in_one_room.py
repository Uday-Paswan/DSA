"""
Problem: N Meetings in One Room
Platform: GeeksforGeeks
Difficulty: Easy

Pattern:
- Greedy
- Sorting
- Activity Selection

Approach:
The goal is to select the maximum number of non-overlapping
meetings that can be conducted in one room.

1. Create pairs of (start, end) for every meeting.
2. Sort the meetings by their finishing time.
3. Select the first meeting.
4. For every next meeting:
   - If its start time is greater than the finish time
     of the previously selected meeting, select it.
5. Count the selected meetings.

Why Greedy?
Choosing the meeting that finishes earliest leaves the maximum
amount of time available for the remaining meetings.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""
def maxMeetings(start, finish):
        
        meetings = []

        for i in range(len(start)):
            meetings.append((finish[i], start[i]))

        meetings.sort()

        count = 0
        last_end = -1

        for end_time, start_time in meetings:

            if start_time > last_end:
                count += 1
                last_end = end_time

        return count

#Test  case
start = [10,12,20]
finish = [20,25,30]
print(maxMeetings(start,finish))