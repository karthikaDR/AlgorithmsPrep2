
# if len(nums) == 0:
#     return 0
# if len(nums) == 1:
#     return nums[0]
# dict1 = {}
# max1 = nums[0] + nums[1]
# array = []
# array1 = []
# array.append(nums[0])
# array.append(nums[1])
# left = 0
# right = 1
# result = sys.maxsize
# while right < len(nums) - 1:
#     right += 1
#     max2 = max1 + nums[right] 
    
#     num = max(max2, max1)
#     if num == max2:
#         max1 = max2
#         array.append(nums[right])                
        
#     else:
        
#         array1.append(max1)
#         result = max2 - nums[left]        
#         max1 = result
#         left += 1
#         array.append(nums[right])
#         array.pop(0)

# print(result, array1)      
#Kadane`s algorithm ---> First check if the addition of the current element reduces
#the sum 
#if not, consider the current element and calculate the best sum
nums = [-2,1,-3,4,-1,2,1,-5,4]
import sys
current = 0
bestsum = 0

for i in nums:
    current = max(i, current+i)
    bestsum = max(bestsum,current)


print(bestsum)
