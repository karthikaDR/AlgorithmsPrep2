arr = [1,2,3]
path = []
res = []
def recursion(arr, path, res ):

    
    if not arr:
        res.append(path)
    for i in range(len(arr)):
        xs = arr[:i] + arr[i+1:]        
        recursion(xs, path+[arr[i]], res)
  

print(recursion(arr, path, res))



