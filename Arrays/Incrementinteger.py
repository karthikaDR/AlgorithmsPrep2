#eg [1,2,9] = [1,3,0]
# [9,9] = [1,0,0]
arr = [9,9]

arr[-1] += 1
print(arr[-1])

#Reversed ---> reverses the array and processes the loop but array order does not get changed
for i in range(1,len(arr)):

    if arr[i] != 10:
        break
    else:
        arr[i] = 0
        arr[i-1] += 1
        print(arr[i-1])
print(arr)
#done for cases like 99
if arr[0] == 10:
    arr[0] = 1
    arr.append(0)

print(arr)