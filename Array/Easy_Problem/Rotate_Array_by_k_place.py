k=int(input("Rotate array by k place:"))
nums=[1,2,3,4,5,6,7,8]
n=len(nums)
def rotate (nums,left,right):
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
    
rotate(nums,n-k,n-1)
rotate(nums,0,n-k-1)
rotate(nums,0,n-1)
print(nums)