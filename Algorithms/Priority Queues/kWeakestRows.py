from collections import defaultdict
import heapq


def kWeakestRows(mat: list[list[int]], k: int) -> list[int]:

    # create a hashmap count number of soldiers 1's:
    countOnes = defaultdict()
    for i in range(len(mat)):
        countOnes[i] = 0
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                countOnes[i] += 1
    
    heap = [(value, key) for key, value in countOnes.items()]
    print(heap)
    heapq.heapify(heap)
    res = []
    while k > 0:
        res.append(heapq.heappop(heap)[1])
        k -= 1

    print(res)
    return res

kWeakestRows([[1,0],[0,0],[1,0]], 2)