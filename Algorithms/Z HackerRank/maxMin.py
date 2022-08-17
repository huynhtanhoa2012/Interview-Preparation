def maxMin(k, arr):
    minimum = float("inf")
    arr.sort()
    for i in range(len(arr)+1-k):
        if arr[k-1+i] - arr[i] < minimum:
            minimum = arr[k-1+i] - arr[i]

    return minimum




maxMin(4, [1,2,3,4,10,20,30,40,100,200]):