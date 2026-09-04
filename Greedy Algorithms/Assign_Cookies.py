"""
Problem: Assign Cookies
Platform: LeetCode
Problem Number: 455
Difficulty: Easy

Pattern:
- Greedy
- Sorting
- Two Pointers

Approach:
Each child has a greed factor g[i], and each cookie has a size s[i].

A child can be satisfied if:
cookie size >= child's greed factor.

1. Sort both arrays.
2. Use two pointers:
   - child → current child
   - cookie → current cookie
3. If the cookie can satisfy the child:
   - Count the child as satisfied.
   - Move to the next child.
4. Always move to the next cookie.
5. Return the number of satisfied children.

Why Greedy?
Try to satisfy the least greedy child with the smallest
cookie that can satisfy them. This preserves larger cookies
for children with higher greed factors.

Time Complexity: O(n log n + m log m)
Space Complexity: O(1) auxiliary space
"""

def assign_cookies(g,s):
    n=len(g)
    m=len(s)
    left=0
    right=0
    count=0
    g.sort()
    s.sort()
    while left<n and right<m:
        if g[left]<=s[right]:
            count+=1
            left+=1
        right+=1
    return count

#Test case
g = [1,2,3]
s = [1,1]
print(assign_cookies(g,s))        