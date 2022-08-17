import heapq
def findKthLargest(nums: list[int], k: int) -> int:
    res = 0
    # 1. construct and add elements into a maxheap
    nums = [-x for x in nums]
    heapq.heapify(nums)

    # 2. Traversing and deleting the top element
    while k > 0:
        # pop element
        res = -1 * heapq.heappop(nums)
        k -= 1
    return res

findKthLargest([3,2,1,5,6,4], 2)