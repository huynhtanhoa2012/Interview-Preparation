def missingNumbers(arr, brr):
    arr1 = [0]* 10004 
    brr1 = [0]* 10004
    res = []
    for i in arr:
        arr1[i] += 1
    for i in brr:
        brr1[i] += 1

    for i in range(10000):
        if brr1[i] > arr1[i]:
            res.append(i)
    print(res)
    return res

missingNumbers([2,3,5], [1,2,2,3,4,5,6,7])

# 3670 3674 3677 3684 3685 3685 3695 3714 3720
# 3670 3674 3677 3684      3685 3695 3714 3720