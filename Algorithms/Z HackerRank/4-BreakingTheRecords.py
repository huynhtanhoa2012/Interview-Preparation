def breakingRecords(scores):
    minRecord = 0
    maxRecord = 0
    currentMinRecord = scores[0]
    currentMaxRecord = scores[0]
    for i in range(1, len(scores)):
        if scores[i] > currentMaxRecord:
            print("Max", scores[i])
            maxRecord += 1
        if scores[i] < currentMinRecord:
            print("Min", scores[i])
            minRecord += 1

    return [maxRecord, minRecord]


breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1])