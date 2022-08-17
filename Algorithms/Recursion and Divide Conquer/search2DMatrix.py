def searchMatrix(arr: list[list[int]], k: int):

    def binarySearch(arr, row_mid, low, high, k):
        while low<=high:
            mid = (low+high)//2
            if arr[row_mid][mid] == k:
                return 1
            elif arr[row_mid][mid] > k:
                high = mid-1
            else:
                low = mid+1
        return 0
    
    rows = len(arr)-1
    cols = len(arr[0])-1
    # Edge cases:
    if arr[0][0] > k or arr[rows][cols] < k:
        return 0

    low, high = 0, rows
    while low<=high:
        mid = (low+high)//2
        if arr[mid][0] <= k and k <= arr[mid][cols]:
            return binarySearch(arr, mid, 0, cols, k)
        elif arr[mid][0] > k:
            high = mid-1
        else:
            low = mid+1
    return 0

searchMatrix([[23, 25, 35, 37],
          [40, 41, 42, 43],
          [50, 60, 74, 80]], 41)
