#Sort the min execution time so that we get min waiting time
# 
# 
arr = [0,5,3,1,2]

arr.sort()
temp = 0
temp1 = 0
arr1 = []
for i in range(1, len(arr)):
    
    temp += arr[i-1]
    temp1 += temp

print(temp1)