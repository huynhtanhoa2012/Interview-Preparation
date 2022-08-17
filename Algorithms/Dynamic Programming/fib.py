def fib(n: int) -> int:
    # base cases:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # create a list to store subproblems solution
    fib = [0]* (n+1)
    fib[0] = 0
    fib[1] = 1

    for i in range(2, n+1):
        fib[i] = fib[i-1] +fib[i-2]
    
    return fib[n]

def fib(n: int) -> int:
    
    def fibonacci(n):
        # base cases:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
        return memo[n]
    
    memo = {}
    return fib(n)