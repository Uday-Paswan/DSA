"""
Problem: Subsets
Platform: LeetCode
Link: https://leetcode.com/problems/subsets/
Difficulty: Medium

Pattern:
- Backtracking
- Recursion

Approach:
At each index, make two choices:
1. Include the current element in the subset.
2. Exclude the current element from the subset.
When the index reaches the end of the array, add a copy of the
current subset to the result. This generates all possible subsets.

Time Complexity: O(n × 2^n)
Space Complexity: O(n) (excluding the output)

"""
def subsets(nums):
    result=[]
    def func(index,subset):
        if index>=len(nums):
            result.append(subset.copy())
            return
        subset.append(nums[index])
        func(index+1,subset)
        subset.pop()
        func(index+1,subset)
    func(0,[])
    return result

#Test Case
nums = [1,2,3]
print(subsets(nums))    