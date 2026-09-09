"""
Problem: Minimum Platforms
Platform: GeeksforGeeks
Difficulty: Medium

Pattern:
- Greedy
- Sorting
- Two Pointers

Approach:
We need to find the minimum number of platforms required so that
no train has to wait.

1. Sort arrival times.
2. Sort departure times.
3. Use two pointers:
   - i → next arriving train
   - j → next departing train
4. If arrival[i] <= departure[j]:
   - A train arrives before the current train leaves.
   - Need one more platform.
   - Move i.
5. Otherwise:
   - A train has departed.
   - One platform becomes free.
   - Move j.
6. Keep track of the maximum number of platforms used.

Time Complexity: O(n log n)
Space Complexity: O(1) auxiliary space
"""
def minimum_platform(arr,dep):
    arr.sort()
    dep.sort()
    i=0
    j=0
    max_platform=0
    platform=0
    while i<len(arr) and j<len(dep):
        if arr[i]<dep[j]:
            platform+=1
            max_platform=max(max_platform,platform)
            i+=1
        else:
            platform-=1
            j+=1
    return max_platform
#Test Case
arr= [900, 940, 950, 1100, 1500, 1800]
dep= [910, 1200, 1120, 1130, 1900, 2000]
print(minimum_platform(arr,dep))