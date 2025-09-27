# Problem: Selection Sort (GeeksforGeeks)
# Link: https://practice.geeksforgeeks.org/problems/selection-sort/1
# Approach: Implemented Selection Sort in Python
# Time Complexity: O(n^2)
# Space Complexity: O(1)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
