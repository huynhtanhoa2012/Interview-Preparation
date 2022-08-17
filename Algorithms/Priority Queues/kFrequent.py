import heapq
def topKFrequent(nums: list[int], k: int) -> list[int]:
    # 1. Use hashmap to store frequencies of each element:
        res = []
        mp = dict()
        for i in nums:
            if i not in mp:
                mp[i] = 1
            else:
                mp[i] += 1

        # Using heapq data structure
        heap = [(value, key) for key, value in mp.items()]

        # Get the top k elements
        largest = heapq.nlargest(k, heap)

        # Print the top k elements
        for i in range(k):
            res.append(largest[i][1])
        
        return res



topKFrequent([1,1,1,2,2,3], 2)