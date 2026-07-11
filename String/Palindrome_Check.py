def palindrome_Check(s):
    n=len(s)
    left=0
    right=n-1
    while left<right:
        if s[left]==s[right]:
            left+=1
            right-=1
        else:
            return False
    return True

#Test case
s="Uday"
print(palindrome_Check(s))