#Search a target element in a sorted 2D matrix.
#Can do O(N*M) search but since the matrix elements are sorted, can do binary search
def findrow(low,high,target):

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

target = 16
low = 0
high = len(matrix)

while low < high:
    mid = low + (high-low) //2

    if matrix[mid] 