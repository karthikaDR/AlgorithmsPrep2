# Given an array of integers, find out whether there are two distinct indices i and j
# in the array such that the absolute difference between nums[i] and nums[j] is at most t 
# and the absolute difference between i and j is at most k.


#Sliding window technique 
#Time Complexity ---> O(n*k)

        #Sliding window technique 
    #Time Complexity --- O(n*k)
def containsNearbyAlmostDuplicate(nums, k, t):
    print(nums,k,t)
    for i in range(len(nums)):
        if i == len(nums) - 1:
            return False

        for j in range(i+1, i+k+1):
            
            if j <= len(nums) - 1:                  
            
                if abs(nums[j] - nums [i]) <= t:
                    return True
        
    return False


if __name__ == "__main__":
   
    arr = [1,2,3,1]
    k= 3
    t = 0
    print(containsNearbyAlmostDuplicate(arr, k, t))