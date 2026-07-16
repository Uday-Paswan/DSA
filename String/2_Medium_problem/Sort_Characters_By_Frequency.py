"""
Problem: Sort Characters By Frequency
Platform: LeetCode
Link: https://leetcode.com/problems/sort-characters-by-frequency/
Difficulty: Medium

Pattern:
- String
- Hash Map
- Sorting

Approach:
Count the frequency of each character using a hash map.
Sort the characters based on their frequencies in descending
order and append each character to the result according to
its frequency.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

def sort_character(s):
    freq={}
    result=""
    for ch in s:
        if ch not in freq:
            freq[ch]=1
        else:
            freq[ch]+=1

    sorted_items=sorted(freq.items(),key=lambda pair:pair[1],reverse=True)

    for ch,count in sorted_items:
        result+=ch*count
    
    return result

#Test case
s = "Aabb"
print(sort_character(s))