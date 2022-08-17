def countingSort(arr):
    # Write your code here
    res = [0]* len(arr)

    for i in arr:
        res[i] += 1
    return res




countingSort([1,1,3,2,1])