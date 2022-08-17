def rob(nums: list[int]) -> int:

    # Take care base cases
    if not nums:
        return 0
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums[0], nums[1])
    
    # Bottom-up: create an array to store solution of subproblem
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    print(dp[0], dp[1])

    for i in range(2, len(nums)):
        dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
    return dp[len(nums)-1]

rob([2,7,9,3,1])