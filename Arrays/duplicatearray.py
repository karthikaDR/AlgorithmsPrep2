nums = [0,0,1,1,1,2,2,3,3,4]
count = 1
num1 = nums[0]
length = len(nums) - 1 
print(length)
i = 0

while (0 <= i <= length):
    if num1 == nums[i] & i <= len(nums):
        del nums[i]
        i = i + 1
    else:
        count = count + 1
        num1 = nums[i]


print(count) 