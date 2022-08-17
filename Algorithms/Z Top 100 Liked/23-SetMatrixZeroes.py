def setZeroes(matrix: list[list[int]]):
    m = len(matrix)
    n = len(matrix[0])

    rows = []
    cols = []
    # find all zeroes:
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows.append(i)
                cols.append(j)
    
    # change all rows
    for i in rows:
        for j in range(n):
            matrix[i][j] = 0
    # change all cols
    for j in cols:
        for i in range(m):
            matrix[i][j] = 0

    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()

setZeroes([[1,1,1],[1,0,1],[1,1,1]])
