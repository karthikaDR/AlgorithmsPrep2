def two_sum(index, char,nums):
        
    i = index
    j = len(nums) -1
    
    while i < j:
        if nums[i] + nums[j] == char:  
            if char == 0:                        
                output.append([char, nums[i], nums[j]])
            else:
                output.append([-1*char, nums[i], nums[j]])                    
            i += 1
            j -= 1
            
        elif nums[i] + nums[j] < char:
            i += 1
            
        else:
            j = j-1

# It is saying three numbers = 0
#meaning two numbers equal to (- or +) third number
#sort is O(nlogn) complexity
#then for and while loop is O(n^2)
#Overall complexity is O(n^2)
output = []
#sort the characters so that if ther eare repetitive charactes we can skip
nums.sort()
for i, char in enumerate (nums):                        
    if len(nums) == 3:
       if (nums[i] + nums[i+1] + nums[i+2]) == 0:
            output.append([nums[i],nums[i+1],nums[i+2]])
            break
            
    if char != 0:
    char = (-1) * char  
    if nums[i] == nums[i-1]:
            continue
                    
    if i < len(nums) - 3:
       two_sum(i+1, char)
        
        
    return output
    
        # x+y+z = 0 means that x+y = -z.
        
 


arr = Solution()
print(arr.threeSum)
        