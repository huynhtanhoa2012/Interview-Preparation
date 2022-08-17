def findBitonic(arr: list[int], element: int) -> int:
    def searchLeftPeak(arr: list[int], low, high, element) -> int:
        while low <= high:
            mid = (low+high)//2
            if arr[mid] == element:
                return mid
            elif arr[mid] > element:
                return searchLeftPeak(arr, low, mid-1, element)
            else:
                return searchLeftPeak(arr, mid+1, high, element)
        return -1 

    def searchRightPeak(arr: list[int], low, high, element) -> int:
        while low <= high:
            mid = (low+high)//2
            if arr[mid] == element:
                return mid
            elif arr[mid] > element:
                return searchLeftPeak(arr, mid+1, high, element)
            else:
                return searchLeftPeak(arr, low, mid-1, element)
        return -1 

    def findPeak(arr: list[int], low, high) -> int:
        if low == high:
            return low
        mid = (low+high)//2
        if arr[mid] > arr[mid+1]:
            return findPeak(arr, low, mid)
        return findPeak(arr, mid+1, high)
    
    # Find index of peak element
    
    peak = findPeak(arr, 0, len(arr)-1)
    if element > arr[peak]:
        return -1
    elif arr[peak] == element:
        return peak
    else:
        temp = searchLeftPeak(arr, 0, peak-1, element)
        if temp != -1:
            return temp
        temp = searchRightPeak(arr, peak+1, len(arr)-1, element)
        if temp != -1:
            return temp
    return -1


findBitonic([-3, 9, 8, 20, 17, 5, 1], 20)



