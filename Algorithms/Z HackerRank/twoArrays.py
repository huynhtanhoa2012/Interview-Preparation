from audioop import reverse


def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        if A[i] + B[i] < k:
            return "NO"
    return "YES"



twoArrays(10, [2, 1, 3], [7, 8, 9])

twoArrays(5, [1, 2, 2, 1], [3, 3, 3, 4])