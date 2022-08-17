from collections import defaultdict


def sockMerchant(n, ar):
    count = 0
    pairs = defaultdict(int)

    for i in ar:
        pairs[i] += 1 
    
    for i in pairs:
        count += pairs[i] // 2

    print(count)


sockMerchant(7, [1,2,1,2,1,3,2])