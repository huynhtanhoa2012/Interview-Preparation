def balancedSums(arr):
    # Write your code here
    n = len(arr)

    suffixLeft = [0] * n
    suffixRight = [0] * n

    suffixLeft[0] = arr[0]
    suffixRight[n-1] = arr[n-1]

    for i in range(1, n):
        suffixLeft[i] = suffixLeft[i-1] + arr[i]
    
    for i in range(n-2, -1, -1):
        suffixRight[i] = suffixRight[i+1] + arr[i]

    for i in range(n):
        if suffixLeft[i] == suffixRight[i]:
            return "YES"
    
    return "NO"

balancedSums([1,2,3,3])
    