def spiralOrder(matrix: list[list[int]]) -> list[int]:
    left, right = 0, len(matrix[0]) - 1
    top, bottom = 0, len(matrix) - 1
    res = []
    while (left<=right and top <=bottom):
        # traverse from left to right
        for i in range(left, right+1):
            res.append(matrix[top][i])
        # shift top 1
        top += 1

        # traverse from top to bottom
        for i in range(top, bottom+1):
            res.append(matrix[i][right])
        # shift right 1
        right -= 1

        if not (left<=right and top <=bottom):
            break

        # traverse from right to left
        for i in range(right, left-1, -1):
            res.append(matrix[bottom][i])
            print(right, left)
        # shift bottom
        bottom -= 1

        # traverse from bottom to top
        for i in range(bottom, top-1, -1):
            res.append(matrix[i][left])
        # shift left
        left += 1
    
    return res


spiralOrder([[1,2,3]])
