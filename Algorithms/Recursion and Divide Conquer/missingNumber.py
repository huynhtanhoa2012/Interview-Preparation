def getMissingNumber(arr: list[int]) -> int:
    
    nums = set()
    for i in range(len(arr)):
        nums.add(arr[i])
    for i in range(len(arr)):
        if i not in nums:
            return i
    return len(arr)

