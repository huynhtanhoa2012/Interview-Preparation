"""
visited = a new set
queue = a new queue
enqueue (0, 0, 1)
add (0, 0) to visited

while the queue is not empty:

    row, col, distance = dequeue and unpack a cell
    if (row, col) is the bottom right cell:
        return distance

    for each open neighbour:
        if neighbour is in visited:
            continue
        otherwise, add neighbour to visited
        enqueue (neighbour_row, neighbour_col, distance + 1)

return -1
"""

def shortestPathBinaryMatrix(grid: list[list[int]]) -> int:

    max_row = len(grid) - 1
    max_col = len(grid[0]) - 1
    # All neighbors of node includes north, west, east, south, diagonals
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def get_neighbors(row, col):
        for row_difference, col_difference in directions:
            new_row = row + row_difference
            new_col = col + col_difference

            # Skip invalid cells
            if not (0 <= new_row <= max_row and 0 <= new_col <= max_col):
                continue
            # Traverse only 0's cell
            if grid[new_row][new_col] != 0:
                continue
            yield (new_row, new_col)

    # Check that the first and last cells are open. 
    if grid[0][0] != 0 or grid[max_row][max_col] != 0:
        return -1

    # Breath First Search
    queue = [(0,0,1)]
    visited = set((0,0))

    while queue:
        row, col, distance = queue.pop(0)
        if (row,col) == (max_row, max_col):
            return distance
        # Traverse all of neighbors
        for neighbor in get_neighbors(row, col):
            if neighbor in visited:
                continue
            visited.add(neighbor)
            # Note that the * splits neighbour into its values.
            queue.append((*neighbor, distance+1))
    
    return -1