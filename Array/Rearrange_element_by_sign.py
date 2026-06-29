"""
Problem: Rearrange Array Elements by Sign
Platform: LeetCode
Link: https://leetcode.com/problems/rearrange-array-elements-by-sign/
Difficulty: Medium

Pattern:
- Array
- Two Pointers

Approach:
Create a new array of the same size.
Place positive numbers at even indices and negative numbers at odd indices.
Return the rearranged array.

Time Complexity: O(n)
Space Complexity: O(n)
"""
def rearrange_element(nums):
    n=len(nums)
    result=[0]*len(nums)
    positive_index=0
    negative_index=1
    for i in range(0,n):
        if nums[i]>0:
            result[positive_index]=nums[i]
            positive_index+=2
        else:
            result[negative_index]=nums[i]
            negative_index+=2
    return (result)

#Test case
nums = [3,1,-2,-5,2,-4]
print(rearrange_element(nums))
        

