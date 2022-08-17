# Iterative
def searchRange(arr: list[int], target: int) -> list[int]:
    
    def searchOccurences(arr, target, firstOrLast: bool) -> int:
        first, last = -1, -1
        low, high = 0, len(arr)-1
        
        while low<=high:
            mid = (low+high)//2
            if arr[mid] == target:
                if firstOrLast:
                    first = mid
                    high = mid-1
                else:
                    last = mid
                    low = mid+1

            elif arr[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return first if firstOrLast else last
    first = searchOccurences(arr, target, True)
    last  = searchOccurences(arr, target, False)

    return [first, last]

# Recursive
def searchRange(arr: list[int], target: int) -> list[int]:
    temp = -1
    def binarySearch(arr, low, high, target, firstOrLast, temp) -> int:
        
        if low > high:
            return temp
        mid = (low+high)//2
        if arr[mid] == target:
            if firstOrLast:
                temp = mid
                return binarySearch(arr, low, mid-1, target, firstOrLast, temp)
            else:
                temp = mid 
                return binarySearch(arr, mid+1, high, target, firstOrLast, temp)
        elif arr[mid] < target:
            return binarySearch(arr, mid+1, high, target, firstOrLast, temp)
        else:
            return binarySearch(arr, low, mid-1, target, firstOrLast, temp)
    
    first = binarySearch(arr, 0, len(arr)-1, target, True, temp)
    last = binarySearch(arr, 0, len(arr)-1, target, False, temp)
    
    return [first, last]

searchRange([1, 3, 5, 5, 5, 5 ,28, 37, 42], 5)
