
def migratoryBirds(arr):
    freq = [0] * 6
    count = 0
    res = 0

    for i in arr:
        freq[i] += 1
    
    for i in range(1, 6):
        if freq[i] > count:
            res = i
            count = freq[i]

    print(res)


migratoryBirds([0,0,1,1,1,2,2,3])