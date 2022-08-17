
def minimumAbsoluteDifference(arr):

    # Write your code here
    arr.sort()
    minimumAbs = float("inf")
    for i in range(len(arr)-1):
        if abs(arr[i] - arr[i+1]) < minimumAbs:
            minimumAbs = abs(arr[i] - arr[i+1])

    print(minimumAbs)
    return minimumAbs


minimumAbsoluteDifference([-2,2,4])