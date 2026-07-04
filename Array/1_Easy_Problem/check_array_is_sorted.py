def is_sorted(arr):
    n=len(arr)
    for i in range(0,n-1):
        if arr[i]>arr[i+1]:
            return False
    return True

# arr=[3,2,10,5,6,12,87]
arr=[1,2,3,4,5,6,7]
print(is_sorted(arr))