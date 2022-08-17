from collections import defaultdict


def singleNumber( nums: list[int]) -> int:
    hashmap = defaultdict()

    for i in nums:
        if i not in hashmap:
            hashmap[i] += 1
    for i in nums:
        if hashmap[i] == 1:
            return hashmap[i]

singleNumber([2,2,1])