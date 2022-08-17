import heapq
def lastStoneWeight(self, stones: list[int]) -> int:
    
    # Add stones into heap
    stones = [-s for s in stones]
    heapq.heapify(stones)

    # continue when length of stones > 1
    while len(stones) > 1:
        s1 = heapq.heappop(stones)
        s2 = heapq.heappop(stones)
        res = abs(s1) - abs(s2)
        if res > 0:
            heapq.heappush(stones, -res)
            
    stones.append(0)
    return abs(stones[0])