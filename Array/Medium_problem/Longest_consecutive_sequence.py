"""
Problem: Longest Consecutive Sequence
Platform: LeetCode
Link: https://leetcode.com/problems/longest-consecutive-sequence/
Difficulty: Medium

Pattern:
- Array
- Hash Set

Approach:
Store all elements in a hash set for O(1) lookup.
Start counting only if the current number is the beginning of a sequence.
Continue checking consecutive numbers and update the longest sequence length.

Time Complexity: O(n)
Space Complexity: O(n)
"""
def sequence(nums):
    my_set=set()
    longest_cons=0
    for i in range(0,len(nums)):
        my_set.add(nums[i])
    
    for num in my_set:
        if num-1 not in my_set:
            current=num
            count=1
            while num+1 in my_set:
                count+=1
                num+=1
            longest_cons=max(longest_cons,count)
    return (longest_cons)

#Test case
nums = [100,4,200,1,3,2]
print(sequence(nums))