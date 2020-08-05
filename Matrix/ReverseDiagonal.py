arr = [[1,2,3],
       [4,5,6],
       [7,8,9]]
N = len(arr[0])
i = 0
j = N


while i<j :
    #reversing major diagonal elements
    arr[i][i], arr[j-1][j-1] = arr[j-1][j-1], arr[i][i]
    #reversing minor diagonal elements
    arr[i][j-1], arr[j-1][i] = arr[j-1][i], arr[i][j-1]


    i += 1
    j -= 1

print(arr)