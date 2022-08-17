# def arrIndexDifference(arr: list[int]) -> int:
#     if len(arr) < 2:
#         return 0

#     maxValue = -1
#     for i in range(len(arr)):
#         j = len(arr) - 1
#         while i < j:
#             if arr[i] < arr[j]:
#                 maxValue = max(maxValue, j-i)
#             j -= 1
#     print(maxValue)
#     return maxValue

def arrIndexDifference(arr: list[int]) -> int:
    index = dict()
    for i in range(len(arr)):
        index[arr[i]] = i
    arr
    





arrIndexDifference([5, 2, 3, 5, 4, 6, 7, 8, 19, 0])
# arrIndexDifference([0, 2, 3, 4, 5, 8, 9])
# arrIndexDifference([11, 8, 5, 4, 2, 1])
