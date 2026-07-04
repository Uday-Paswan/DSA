nums=[1,5,8,2,4,9]
target=int(input("Targeted element:"))
def linear_Search(nums):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
    return -1
print(linear_Search(nums))
