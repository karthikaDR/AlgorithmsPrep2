#Time Complexity ----> O(n)
#Given an array of integers and an integer k, find out whether there are two distinct indices
# i and j in the array such 
# that nums[i] = nums[j] and the absolute difference between i and j is at most k.


def containsNearbyDuplicate(nums, k):
    dict = {}
    
    for index, value in enumerate(nums):
        if (value in dict) and ((index - dict[value]) <= k):
            return True
        
        dict[value] = index
    return False


if __name__ == "__main__":
    arr = [1,2,3,1]
    k = 3
    print(containsNearbyDuplicate(arr,k))

