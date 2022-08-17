def canJump(nums: list[int]) -> bool:
    lastIndex = len(nums) - 1

    for i in range(lastIndex - 1, -1, -1):
        if i + nums[i] >= lastIndex:
            lastIndex = i
    
    return lastIndex == 0
