def climbStairs(n: int) -> int:
    # Base cases:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2

    # Create a list to store subproblems solution
    step = [0]* (n+1)
    step[1] = 1
    step[2] = 2

    for i in range(3, n+1):
        step[i] = step[i-1] + step[i-2]

    return step[i]


def climbStairs1(n: int) -> int:

    def countStep(n):
        # Base cases:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        
        if n in memo:
            return memo[n]
        memo[n] = countStep(n-1) + countStep(n-2)
        return memo[n]
    
    memo = {}
    return countStep(n)

climbStairs1(3)
    
