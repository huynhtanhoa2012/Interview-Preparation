import heapq


def findKthLargest(nums: list[int], k: int) -> int:
    res = 0
    # 1. construct a max heap
    nums = [-x for x in nums]
    heapq.heapify(nums)

    # 2. pop elements k time
    while k > 0:
        res = -1 * heapq.heappop(nums)
        k -= 1

    # 3. print root element
    return res