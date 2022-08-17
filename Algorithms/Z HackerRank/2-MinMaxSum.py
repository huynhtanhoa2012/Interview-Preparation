def miniMaxSum(arr):
    arr.sort()
    maxSum = 0
    minSum = 0

    # find max sum
    for i in range(4):
        minSum += arr[i]

    # find max sum
    for i in range(4,0,-1):
        maxSum += arr[i]
        
    print(minSum, maxSum)




miniMaxSum([1,3,5,7,9])