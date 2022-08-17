from xmlrpc.client import MAXINT


def minimumAbsDifference(arr: list[int]) -> list[list[int]]:
    
    res = []
    arr.sort()
    minimumAbs = min

    for i in range(len(arr)-1):
        minimumAbs = min(minimumAbs, arr[i+1] - arr[i])
    
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] == minimumAbs:
            res.append([arr[i],arr[i+1]])
    print(res)
    return res

minimumAbsDifference([4,2,1,3])