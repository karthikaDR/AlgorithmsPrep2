nums = [1,1,19,19,4,3,5,5]
res = []

for x in nums:

    if nums[abs(x)-1] < 0:
        res.append(x)
    else:
        nums[abs(x) - 1] *= -1

print(res)
