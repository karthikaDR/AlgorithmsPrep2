nums = [1,1,1,2]
# length = len(nums)
# temp = -1
# for i in range(length):
#     if i == 0:
#         temp = nums[i]
#     else:
#         if nums[i] == temp:
            
#             nums.remove(i)
#         else:
#             temp = nums[i]
# print(nums)

i = 0
for j in range(1, len(nums)) :
    if (nums[j] != nums[i]) :
        i+=1
        nums[i] = nums[j]
print(i+1)
