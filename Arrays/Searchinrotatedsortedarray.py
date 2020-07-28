# # Suppose an array sorted in ascending order is rotated at 
# # some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# You are given a target value to search. If found in the array
#  return its index, otherwise return -1.
# You may assume no duplicate exists in the array.
# Your algorithm's runtime complexity must be in the order of O(log n).

def findelement(self,nums):
    target = 0
    low =0
    high = len(nums) - 1

    # Either left or right side will be sorted for sure.
    # Check which side is sorted using the mid as comparator
    # after determining which side, check the target lies in that area
    # if target lies in the area then decrement the high point 
    #else increment the low point
    while(low < high):
        mid = (low + high)//2
        if target == nums[mid]:
           return mid
        else:
            if (nums[mid] < nums[high]):
                if (nums[mid] < target <= nums[high]):
                    low = mid + 1
                else:
                    high = high - 1

            else:

                if (nums[low] <= target < nums[mid]):
                    high = high - 1
                else:
                    low = mid + 1
    return -1
nums = [4,5,6,7,0,1,2]

if len(nums) == 0:
    print("-1")

print(findelement(nums))


 
        

print("not foundS")
        