def pickingNumbers(a):
    a.sort()
    p1, p2 = 0, 1
    res = 1
    count = 1
    
    while p2 < len(a):
        if a[p2] - a[p1] <= 1:
            count += 1
            res = max(res, count)
        else:
            p1 = p2
            count = 1
        p2 += 1
    
    print(res)
    return res

pickingNumbers([1,1,2,2,4,4,5,5,5])
