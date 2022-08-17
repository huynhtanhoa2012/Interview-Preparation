def plusMinus(arr):
    positive = 0
    negative = 0
    zeros = 0

    for i in arr:
        if i == 0:
            zeros += 1
        elif i > 0:
            positive += 1
        else:
            negative += 1
    
    print("{:.6f}".format(positive/len(arr)))
    print("{:.6f}".format(negative/len(arr)))
    print("{:.6f}".format(zeros/len(arr)))



plusMinus([1,1,0,-1,-1])
    