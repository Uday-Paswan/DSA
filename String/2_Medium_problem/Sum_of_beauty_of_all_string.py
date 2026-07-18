"""
Problem: Sum of Beauty of All Substrings
Platform: LeetCode
Link: https://leetcode.com/problems/sum-of-beauty-of-all-substrings/
Difficulty: Medium

Pattern:
- String
- Hash Map
- Frequency Counting

Approach:
Generate all possible substrings by fixing the starting index.
Maintain the frequency of characters while extending the ending
index. For each substring, compute the beauty as the difference
between the maximum and minimum non-zero character frequencies,
then add it to the final answer.

Time Complexity: O(n² × 26)
Space Complexity: O(26) ≈ O(1)
"""
def sum_of_beauty(s):
    n=len(s)
    ans=0
    for i in range(n):
        freq={}
        for j in range(i,n):
            freq[s[j]]=freq.get(s[j],0)+1
            values=freq.values()
            max_freq=max(values)
            min_freq=min(values)
            ans+=(max_freq-min_freq)
    return ans

#Test Case
s = "aabcbaa"
print(sum_of_beauty(s))
