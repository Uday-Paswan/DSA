"""
Problem: Insertion Sort (GeeksforGeeks)
Link: https://practice.geeksforgeeks.org/problems/insertion-sort/1
Difficulty: Easy

Description:
Insertion sort is a simple sorting algorithm that builds the final sorted array one item 
at a time. It is much less efficient on large lists than more advanced algorithms like 
Merge Sort and Quick Sort, but it is useful for small datasets.

Example:
Input: arr = [4, 1, 3, 9, 7]
Output: [1, 3, 4, 7, 9]

Constraints:
1 <= N <= 10^3
1 <= arr[i] <= 10^3
"""
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr



arr = [4, 1, 3, 9, 7]
print("Sorted array:", insertion_sort(arr))  # Output: [1, 3, 4, 7, 9]
