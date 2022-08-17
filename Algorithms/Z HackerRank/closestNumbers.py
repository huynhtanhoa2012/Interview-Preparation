def closestNumbers(arr):
    # Write your code here
    # 1. loop through array find abs difference
    arr.sort()
    res = []
    minimumAbs = float("inf")
    for i in range(len(arr)-1):
        if abs(arr[i] - arr[i+1]) < minimumAbs:
            minimumAbs = abs(arr[i] - arr[i+1])

    for i in range(len(arr)-1):
        if abs(arr[i] - arr[i+1]) == minimumAbs:
            res.append(arr[i])
            res.append(arr[i+1])

    print(res)
    return res


closestNumbers([-20, -3916237, -357920, -3620601,
 7374819, -7330761, 30, 6246457, -6461594, 266854] )