nums = [0, 1, 2]       
for i in range(len(nums)-1):
    if nums[i] <= 0:
        del nums[i]
nums.sort()
result = 1
print(nums)
for i in range(len(nums)):
    if nums[i] != result:
        print(result)
    result += 1