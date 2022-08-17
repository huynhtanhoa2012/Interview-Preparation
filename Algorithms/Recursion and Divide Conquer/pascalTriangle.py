def getRow(rowIndex: int) -> list[int]:
    res = []
    memoi = {}

    def helper(i,j) -> int:
        # Base case
        if j==0 or i==0 or i==j:
            return 1
        
        if (i,j) not in memoi:
            memoi[(i,j)] = helper(i-1, j-1) + helper(i-1, j)
        
        return memoi[(i,j)]
        # Recurrence relation
    
    for i in range(rowIndex+1):
        res.append(helper(rowIndex, i))
    
    return res

getRow(4)