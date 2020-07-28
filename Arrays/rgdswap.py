arr1 = ['G', 'B', 'R', 'G','B','B','R', 'G','B']
arr = ['G','B','R','R','B','R','G']

left = 0
right = 0

#Get all the 'R' in the first
while right < len(arr) -1 :
    right += 1
    if arr[right] == 'R' and (arr[left] == 'G' or arr[left] == 'B'):
       arr[left], arr[right] = arr[right], arr[left]
       left+=1
#Get the first index where G or R starts
for index, i in enumerate(arr):
    if i == 'G' or i == 'B':
        left, right = index, index + 1
        break
print(left,right)


while right < len(arr) -1 and left < len(arr) - 1:
    # right += 1
    # if arr[right] == arr[left]:
    #     left += 1
    right += 1 
    if arr[right] == 'G' and arr[left] == 'B':
        arr[left], arr[right] = arr[right], arr[left]
        left+=1
    if arr[right] == 'B' and arr[left] == 'G':
        left += 1

    
   
        
print(arr)




