def gamingArray(arr):
    count = 0
    maxNumber = arr[0]
    for i in range(len(arr)-1):
        if arr[i] > maxNumber:
            count += 1
            maxNumber = arr[i]
    
    if count%2==1:
        return "BOB"
    else: 
        return "ANDY"


gamingArray([2,3,5,4,1])