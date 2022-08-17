def waveArray(arr: list[int]) -> list[int]:


    # Lexicographically smallest => list should be sorted
    arr.sort()
    
    # 1. Loop through entire array:
    for i in range(len(arr) - 1):
        # case 1: index is even. Check if arr[i] < arr[i+1]
        if i%2==0 and arr[i]<arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        # case 2: index is odd. Check if arr[i] > arr[i+1]
        if i%2==1 and arr[i]>arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr
