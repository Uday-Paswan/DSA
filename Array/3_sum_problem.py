def Three_sum(nums):
    n=len(nums)
    result=[]
    nums.sort()
    for i in range(n-2):
        left=i+1
        right=n-1
        if i>0 and nums[i]==nums[i-1]:
            continue
        if nums[i]>0:
            break
        while left<right:
            sums=nums[i]+nums[left]+nums[right]
            if sums==0:
                result.append([nums[i],nums[left],nums[right]])
                left+=1
                right-=1
                while left<right and nums[left]==nums[left-1]:
                    left+=1
                while left<right and nums[right]==nums[right+1]:
                    right-=1
            elif sums<0:
                left+=1
            elif sums>0:
                right-=1
    return result

#Test Case
nums=[-1,0,1,2,-1,-4]
print(Three_sum(nums))        
    
            
