def birthday(s, d, m):
    count = 0
    for i in range(len(s)-m+1):
        current = 0
        for j in range(i, m+i):
            current += s[j]
        if current == d:
            count += 1
    
    print(count)
    return count

birthday([2, 5, 1 ,3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1,
], 18, 7)

