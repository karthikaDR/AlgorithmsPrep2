max_sum = 0
window_sum = 0
k = 4 
arr = [-2,1,-3,4,-1,2,1,-5,4]
#[16,2,9,4,5, 6, 7, 9]
#calculate sum of 1st window */
for i in range(0, k):
  window_sum += arr[i]
#slide window from start to end in array. */

max_sum = window_sum
for j in range(k, len(arr)): 
    print(arr[j], arr[j-k], j-k)
    window_sum += arr[j] - arr[j-k]   
    
    max_sum = max(max_sum, window_sum)
print(max_sum)
