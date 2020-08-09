           
def repeating(arr):        
           
   for i in range(len(arr)): 
        if arr[abs(arr[i])-1] > 0: 
            arr[abs(arr[i])-1] = -arr[abs(arr[i])-1] 
        else: 
            print("The repeating element is", abs(arr[i])) 
              
   for i in range(len(arr)): 
        if arr[i]>0: 
            print("and the missing element is", i + 1) 

nums = [1,3,4,2,2]
print(repeating(nums))