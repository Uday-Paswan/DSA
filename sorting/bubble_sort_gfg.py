"""
Problem: Bubble Sort (GeeksforGeeks)
Link: https://practice.geeksforgeeks.org/problems/bubble-sort/1
Difficulty: Easy

Description:
Bubble Sort is a simple sorting algorithm that works by repeatedly swapping the adjacent 
elements if they are in the wrong order. This process continues until the array is sorted.

Example:
Input: arr = [4, 1, 3, 9, 7]
Output: [1, 3, 4, 7, 9]

Constraints:
1 <= N <= 10^3
1 <= arr[i] <= 10^3
"""
def bubbleSort(arr):
        n=len(arr)
        for i in range(n-1):
            swap=False
            for j in range(n-i-1):
                if(arr[j]>arr[j+1]):
                    arr[j],arr[j+1]=arr[j+1],arr[j]
                    swap=True
            if (swap==False):
                return
            
arr=[4, 1, 3, 9, 7]
bubbleSort(arr)
print(arr)