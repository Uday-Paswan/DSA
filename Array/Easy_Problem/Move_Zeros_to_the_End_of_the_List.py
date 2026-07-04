nums=[0,1,0,3,12]
def move_zero(nums):
    # if len(nums)==1:
    #     return
    # i=0
    # while i<len(nums):
    #     if nums[i]==0:
    #         break
    #     i+=1
    # if i==len(nums):
    #     return
    # j=i+1
    # while j<len(nums):
    #     if nums[j]!=0:
    #         nums[i],nums[j]=nums[j],nums[i]
    #         i+=1
    #     j+=1
    i=0
    for j in range(len(nums)):
        if nums[j]!=0:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
move_zero(nums)
print(nums)
