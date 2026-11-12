"""
Problem: Word Ladder
Platform: LeetCode
Link: https://leetcode.com/problems/word-ladder/
Difficulty: Hard

Pattern:
- Graph
- Breadth-First Search (BFS)
- Shortest Path
- Implicit Graph

Approach:
Treat each word as a node in a graph.
Two words are connected if they differ by exactly one character.
Start BFS from beginWord and generate all possible one-character transformations.
If a generated word exists in the word list and has not been visited, add it to the queue.
Track the transformation sequence length at each BFS level.
Return the length when endWord is reached; otherwise, return 0.

Time Complexity: O(N * L * 26 * L)
Space Complexity: O(N * L)

Where:
N = Number of words in wordList
L = Length of each word
"""
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordset=set(wordList)
        if endWord not in wordset:
            return 0
        queue=deque()
        queue.append((beginWord,1))
        while queue:
            curr_word,level=queue.popleft()
            if curr_word==endWord:
                return level
            for i in range(len(curr_word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch==curr_word[i]:
                        continue
                    new_word=curr_word[:i]+ch+curr_word[i+1:]
                    if new_word in wordset:
                        queue.append((new_word,level+1))
                        wordset.remove(new_word)
        return 0
                        