def waveArray(arr: list[int]) -> list[int]:

    arr.sort()
    for i in range(len(arr) - 1):
        if i%2==0 and arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr