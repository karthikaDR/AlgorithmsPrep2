arr = [5, 6, 7, 1, 4, 0,-1]

pivot = arr[3]

small,equal, large = 0, 0, len(arr)-1

#bring all the smaller elements than pivot to the left side,
#Bring all the greater elements to the right of the pivot
#Complexity ---> O(n), Space Complexity ---> O(1)
while equal < large :
    if arr[equal] < pivot:
        arr[equal],arr[small] = arr[small], arr[equal]
        small += 1
        equal += 1
    elif arr[equal] == pivot:
        equal += 1
    else:
        
        arr[equal], arr[large] = arr[large], arr[equal]
        large -= 1
     

print(arr)
# #Reversing the list to makethe loop end faster
# for j in reversed(range(len(arr))):

#     if arr[i] < pivot:
#         break
#     else:
        
#         arr[i], arr[large] = arr[large], arr[i]
#         large -= 1
        

# print(arr)

