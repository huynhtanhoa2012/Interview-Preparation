def selectionSort(arr: list[int]) -> list[int]:

    # Loop entire array to n-2
    for i in range(len(arr)-1):
        # Variable to store index of minimum value in array
        indexMin = i
        # Loop through the rest of array to find minimum value
        for j in range(i+1, len(arr)):
            if arr[j] < arr[indexMin]:
                indexMin = j    # store index of minimum value  

        # swap the element at indexMin and i
        arr[indexMin], arr[i] = arr[i], arr[indexMin]

    print(arr)
    return arr
selectionSort([5, 2, 3, 1])