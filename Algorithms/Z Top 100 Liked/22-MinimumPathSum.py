def minPathSum(grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    # Initiallize value for first row and first column
    for j in range(1,n):
        grid[0][j] = grid[0][j] + grid[0][j-1]
    for i in range(1,m):
        grid[i][0] = grid[i][0] + grid[i-1][0]

    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
            
    return grid[m-1][n-1]

minPathSum([[1,2,3],[4,5,6]])