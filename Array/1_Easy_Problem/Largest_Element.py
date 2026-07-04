arr=[1,6,77,55,33,45,32]
def largest_element(arr):
    largest=float("-inf")
    for i in range(0,len(arr)):
        if largest<arr[i]:
            largest=arr[i]
    return largest

result=largest_element(arr)
print(result)