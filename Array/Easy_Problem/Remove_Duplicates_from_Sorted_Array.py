arr=[1,1,2,2,2,3,4,4,5,6,6]
def duplicate(arr):
    n=len(arr)
    i=0
    j=i+1
    if n==1:
        return 1
    while j<n:
        if arr[j]!=arr[i]:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
        j+=1
    return i+1
        
print(duplicate(arr))
