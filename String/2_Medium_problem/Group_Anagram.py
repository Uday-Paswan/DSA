"""
Problem: Group Anagrams
Platform: LeetCode
Link: https://leetcode.com/problems/group-anagrams/
Difficulty: Medium

Pattern:
- String
- Hash Map

Approach:
Sort each string and use the sorted string as the key in a hash
map. Group all strings with the same sorted key together and
return the grouped values.

Time Complexity: O(n × k log k)
Space Complexity: O(n × k)
"""

def group_anagram(s):
    freq={}
    for word in s:
        sort="".join(sorted(word))
        if sort in freq:
            freq[sort].append(word)
        else:
            freq[sort]=[word]
    return list(freq.values())

#Test case
s = ["eat","tea","tan","ate","nat","bat"]
print(group_anagram(s))