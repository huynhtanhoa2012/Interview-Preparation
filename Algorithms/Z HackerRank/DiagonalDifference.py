def diagonalDifference(arr):
    # First diagonal
    first, second = 0, 0
    for i in range(len(arr)):
        first += arr[i][i]
    
    # Second diagonal
    l, r = 0, len(arr) - 1
    while l < len(arr) and r >= 0:
        second += arr[l][r]
        l += 1
        r -= 1
    return abs(first - second)


def diagonalDifference(arr):
    # Write your code here, O(n)
    #l, r = left sum, right sum
    l, r = 0, 0
    # single pass, grab both values
    for i in range(len(arr)):
        l += arr[i][i]
        r += arr[i][-i-1] # get value in reverse order
    return abs(l-r)