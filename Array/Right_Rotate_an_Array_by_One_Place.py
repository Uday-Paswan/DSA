nums=[1,2,3,4,5,6,7,8]
n=len(nums)
a=nums[n-1]
nums[:]=[nums[n-1]]+nums[0:n-1]
print(nums)