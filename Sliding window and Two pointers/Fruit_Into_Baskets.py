"""
Problem: Fruit Into Baskets
Platform: LeetCode
Problem Number: 904
Difficulty: Medium

Pattern:
- Sliding Window
- Two Pointers
- Hash Map

Approach:
Use a sliding window and a dictionary to store the frequency
of each fruit type in the current window.

We can have at most 2 different types of fruits.

1. Move right to expand the window.
2. Add the current fruit to the dictionary.
3. If the window contains more than 2 fruit types,
   move left until only 2 types remain.
4. Update the maximum window length.

Time Complexity: O(n)
Space Complexity: O(1)
"""
def totalFruit(fruits):

        maxi = 0
        left = 0
        my_dict = {}

        for right in range(len(fruits)):

            my_dict[fruits[right]] = my_dict.get(fruits[right], 0) + 1

            while len(my_dict) > 2:

                my_dict[fruits[left]] -= 1

                if my_dict[fruits[left]] == 0:
                    del my_dict[fruits[left]]

                left += 1

            maxi = max(maxi, right - left + 1)

        return maxi

#Test case
fruits = [0,1,2,2]
print(totalFruit(fruits))