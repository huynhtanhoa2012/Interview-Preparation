def twoSum(nums: list[int], target: int) -> list[int]:
    num_map = {}
    for i in range(len(nums)):
        current = target - nums[i]
        if current in num_map:
            return [num_map[current], i]
        else:
            num_map[nums[i]] = i

    
twoSum([2,7,11,15], 9)