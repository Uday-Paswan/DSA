"""
Problem: 4Sum
Platform: LeetCode
Link: https://leetcode.com/problems/4sum/
Difficulty: Medium

Pattern:
- Array
- Sorting
- Two Pointers

Approach:
Sort the array and fix the first two elements.
Use two pointers to find the remaining two elements whose sum
equals the target. Skip duplicate elements to avoid duplicate
quadruplets.

Time Complexity: O(n³)
Space Complexity: O(1)
"""

def four_sum(nums,target):
    n=len(nums)
    result=[]
    nums.sort()
    for i in range(n-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1,n):
            if j>i+1 and nums[j]==nums[j-1]:
                continue
            left=j+1
            right=n-1
            while left<right:
                total=nums[i]+nums[j]+nums[left]+nums[right]
                if total==target:
                    result.append([nums[i],nums[j],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif total<target:
                    left+=1
                elif total>target:
                    right-=1
    return result

#Test Case
nums = [1,0,-1,0,-2,2]
target = 0
print(four_sum(nums,target))  