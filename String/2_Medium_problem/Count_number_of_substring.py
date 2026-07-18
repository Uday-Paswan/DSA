"""
Problem: Count Number of Substrings With K Distinct Characters
Platform: GeeksforGeeks / Coding Ninjas / Interview Problem
Difficulty: Medium

Pattern:
- String
- Sliding Window
- Hash Map

Approach:
Use the sliding window technique to count the number of
substrings with at most K distinct characters. Then apply
the formula:
Exactly K = AtMost(K) - AtMost(K - 1)

Time Complexity: O(n)
Space Complexity: O(k)
"""
def count_sub(s,k):
    def atMostK(s, k):
        left = 0
        count = 0
        freq = {}

        for right in range(len(s)):
            # Add current character
            freq[s[right]]=freq.get(s[right],0)+1

            # Shrink window while invalid
            while len(freq)>k:
                freq[s[left]]-=1
                if freq[s[left]]==0:
                    del freq[s[left]]
                left+=1


            # Count valid substrings
            count+=right-left+1

        return count
    return atMostK(s,k)-atMostK(s,k-1)

#Test case
s = "pqpqs"
k = 2
print(count_sub(s,k))