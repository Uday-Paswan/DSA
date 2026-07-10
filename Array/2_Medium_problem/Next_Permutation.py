"""
Problem: Next Permutation
Platform: LeetCode
Link: https://leetcode.com/problems/next-permutation/
Difficulty: Medium

Pattern:
- Array
- Two Pointers

Approach:
Traverse the array from right to left to find the first index
where the current element is smaller than the next element.
Swap it with the next greater element on its right, then
reverse the remaining suffix to obtain the next lexicographically
greater permutation.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def next_permutation(nums):
    n=len(nums)
    pivot=-1
    for i in range(n-2,-1,-1):
        if nums[i]<nums[i+1]:
            pivot=i
            break
    if pivot==-1:
        nums.reverse()
        return nums
    for j in range(n-1,pivot,-1):
        if nums[pivot]<nums[j]:
            swap=j
            break
    nums[pivot],nums[swap]=nums[swap],nums[pivot]
    k=pivot+1
    l=n-1
    while k<l:
        nums[k],nums[l]=nums[l],nums[k]
        k+=1
        l-=1
    return nums 
    
#Test Case
nums=[1,2,3]
print(next_permutation(nums))