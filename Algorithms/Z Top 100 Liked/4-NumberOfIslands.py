def numIslands(grid: list[list[str]]) -> int:

    max_row = len(grid) - 1
    max_col = len(grid[0]) - 1
    directions = [(-1, 0),(0, 1),(1, 0),(0, -1)]

    def BFS(row, col):
        q = [(row,col)]
        while q:
            row, col = q.pop(0)
            # traverse all the neighbors horizonally, vertically
            for row_difference, col_difference in directions:
                new_row = row + row_difference
                new_col = col + col_difference
                # only valid row and col
                if 0 <= new_row <= max_row and 0 <= new_col <= max_col:
                    if grid[new_row][new_col] == "1":
                        q.append((new_row, new_col))
                        grid[new_row][new_col] = 0

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                BFS(i, j)
                count += 1

    return count

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

numIslands(grid)