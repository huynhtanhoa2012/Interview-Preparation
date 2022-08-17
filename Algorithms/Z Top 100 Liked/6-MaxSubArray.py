"""
start new array with this item, or continue max sub array

"""

def maxSubArray(nums: list[int]) -> int:
    maxSubArray = nums[0]
    currentSum = 0

    for i in range(len(nums)):
        # start new array with this item, or continue max sub array
        currentSum = max(currentSum + nums[i], nums[i])
        # Check if currentSum >= max Sub array
        if currentSum > maxSubArray:
            maxSubArray = currentSum
    
    return maxSubArray