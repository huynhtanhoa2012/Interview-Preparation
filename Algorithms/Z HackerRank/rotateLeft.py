def rotateLeft(d, arr):
    rotations = d%(len(arr))

    arr = arr[rotations:] + arr[:rotations]
    print(arr)
    return arr
rotateLeft(4, [1,2,3,4,5])