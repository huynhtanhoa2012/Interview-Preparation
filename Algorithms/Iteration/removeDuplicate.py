def removeDuplicates(arr: list[int]) -> int:
    
    if len(arr) == 1:
        return 1
    
    slow = 1
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            arr[slow] = arr[i+1]
            slow += 1

    print(slow)
    return slow

removeDuplicates([-1, 0, 1, 1, 2, 9, 9])