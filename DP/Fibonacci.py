def fibonacci(n, memo):
    
    if memo[n] != -1:
        return memo[n]
    memo[n] = fibonacci(n-2, memo) + fibonacci(n-1,memo)
    return memo[n]
    
    
n = 5
memo = [-1] * (n+1)
memo[0] = 0
memo[1] = 1
print(fibonacci(n, memo))