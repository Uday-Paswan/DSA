"""
Problem: Two Sum
Platform: LeetCode
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy

Pattern:
- Array
- Hash Map

Approach:
Traverse the array while storing each number and its index in a
hash map. For each element, check if its complement
(target - current number) already exists in the hash map.
If found, return both indices.

Time Complexity: O(n)
Space Complexity: O(n)
"""
def two_sum(nums):
    target=6
    n=len(nums)
    hashmap={}
    for i in range(0,n):
        remaining=target-nums[i]
        if remaining in hashmap:
            return [hashmap[remaining],i]
        hashmap[nums[i]]=i
    return[]

#Test case
nums=[3,2,4]
print(two_sum(nums))




