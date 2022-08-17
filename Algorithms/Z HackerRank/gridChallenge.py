def gridChallenge(grid):
    # Write your code here
    
    for row in range(len(grid)):
        grid[row] = sorted(grid[row])

    for col in range(len(grid[0])):
        for row in range(len(grid)-1):
            if grid[row][col] > grid[row+1][col]:
                print("false")
                return False
    print("true")
    return True


gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv'])