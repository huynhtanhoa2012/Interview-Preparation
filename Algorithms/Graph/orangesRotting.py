def orangesRotting(grid: list[list[int]]) -> int:
    if not grid:
        return -1

    # Count fresh oranges
    freshOranges = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                freshOranges += 1
    print("fresh oranges: ", freshOranges)

    # Get all neighbours
    max_row = len(grid) - 1
    max_col = len(grid[0]) - 1
    directions = [(-1,0), (0,1), (1,0), (0,-1)]
    def get_neighbours(row, col) -> list:
        neighbours = []
        for row_difference, col_difference in directions:
            new_row = row + row_difference
            new_col = col + col_difference
            if (new_row, new_col) == 0 or (new_row, new_col) == 2:
                continue
            if 0 <= new_row <= max_row and 0 <= new_col <= max_col:
                neighbours.append((new_row, new_col))
                grid[new_row][new_col] = 2
        return neighbours
    
    # Breadth First Search
    q = [(0,0,0)]   # 0th minute
    visited = set((0,0))
    res = 0

    while q:
        row, col, count = q.pop(0)
        res = count

        for neighbour in get_neighbours(row, col):
            if neighbour in visited:
                continue
            visited.add(neighbour)
            q.append((*neighbour, count+1))
    # Count fresh oranges
    countFreshOranges = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                countFreshOranges += 1
    print("count fresh oranges: ", countFreshOranges)

    if countFreshOranges != 0:
        print(-1)
        return -1
    else: 
        print(res)
        return res

orangesRotting([[2,1,1],[1,1,0],[0,1,1]])