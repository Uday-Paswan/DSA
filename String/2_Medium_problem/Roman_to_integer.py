"""
Problem: Roman to Integer
Platform: LeetCode
Link: https://leetcode.com/problems/roman-to-integer/
Difficulty: Easy

Pattern:
- String
- Hash Map

Approach:
Traverse the string from right to left.
If the current Roman numeral is smaller than the previous one,
subtract its value; otherwise, add its value.
Use a hash map to store the value of each Roman numeral.

Time Complexity: O(n)
Space Complexity: O(1)
"""
def roman_to_integer(s):
    roman={
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    answer=0
    for i in range(len(s)-1):
        if roman[s[i]]<roman[s[i+1]]:
            answer-=roman[s[i]]
        else:
            answer+=roman[s[i]]
    answer=answer+roman[s[-1]]
    return answer

#Test Case
s = "MCMXCIV"
print(roman_to_integer(s))
