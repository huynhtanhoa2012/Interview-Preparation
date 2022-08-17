def matrixZero(arr: list[list[int]]) -> list[list[int]]:
    
    # Create 2 varibales to store position = 0 
    rows, columns = [], []
    for row in range(len(arr)):
        for column in range(len(arr[0])):
            if arr[row][column] == 0:
                rows.append(row)
                columns.append(column)
    
    
    if rows:
        for row in rows:
            for column in range(len(arr[0])):
                arr[row][column] = 0
    
    if columns:
        for column in columns:
            for row in range(len(arr)):
                arr[row][column] = 0

    return arr