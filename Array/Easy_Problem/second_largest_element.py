arr=[1,6,77,55,33,45,32]
def S_largest_element(arr):
    largest=float("-inf")
    s_largest=float("-inf")
    for i in range(0,len(arr)):
        if largest<arr[i]:
            largest=arr[i]
    for i in range(0,len(arr)):
        if s_largest<arr[i] and arr[i]!=largest:
            s_largest=arr[i]
    return s_largest

result=S_largest_element(arr)
print(result)