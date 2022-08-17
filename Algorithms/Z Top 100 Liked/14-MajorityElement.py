from collections import defaultdict


def majorityElement(nums: list[int]) -> int:
        
        hashmap = defaultdict(int)
        maxValue = 0
        res = 0
        
        for i in nums:
            hashmap[i] += 1
        
        for i in hashmap:
            if hashmap[i] > maxValue:
                maxValue = hashmap[i]
                res = i
        
        return res


majorityElement([2,2,1,1,1,2,2])