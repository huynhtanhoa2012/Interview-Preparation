def uniquePaths(m: int, n: int) -> int:
    
    dp = [[1] * n for _ in range(m)]

    for row in range(1,m):
        for col in range(1,n):
            if m==0 or n==0:
                dp[row][col] = 1
            else:
                dp[row][col] = dp[row-1][col] + dp[row][col-1]

    return dp[m-1][n-1]

uniquePaths(3,7)