def maximumPerimeterTriangle(sticks):

    # sort array
    sticks.sort()
    n = len(sticks) - 1

    # traverse from the back
    for i in range(n, 1, -1):
        a = sticks[i-2]
        b = sticks[i-1]
        c = sticks[i]

        if a + b > c:
            return [a,b,c]

    print(-1)
    return [-1]  


maximumPerimeterTriangle([1,2,3])