# p = 1
nums = [1, 2, 3, 4, 5]
# n = len(nums)
# output = []
# for i in range(0,n):
#     output.append(p)
#     p = p * nums[i]
# print(output)
# p = 1
# for i in range(n-1,-1,-1):
#     output[i] = output[i] * p
#     p = p * nums[i]
# print (output)


answer = [1]*len(nums)
answer[0] = 1
for i in range(1, len(nums)):
    answer[i] = answer[i-1] * nums[i-1]
    print(answer[i])
rightProduct = 1
for i in range(len(nums)-1, -1, -1):
    answer[i] = answer[i] * rightProduct
    rightProduct *= nums[i]
print(answer)