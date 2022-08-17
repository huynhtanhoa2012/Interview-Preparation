def minCostClimbingStairs(cost: list[int]) -> int:

    # 1. Define an array minimumCost, 
    # where minimumCost[i] represents the minimum cost of reaching the ith step.
    minimumCost = [0] * (len(cost) + 1)

    # 2. Iterate from 2 because we can start from index 0 or 1 => cost to reach = 0
    for i in range(2, len(cost)+1):
        minimumCost[i] = min(minimumCost[i-1] + cost[i-1], minimumCost[i-2] + cost[i-2])
    
    return minimumCost[len(cost)]


def minCostClimbingStairs(cost: list[int]) -> int:

    def minimumCost(i):
        # Base case, start at index 0 or 1
        if i <= 1:
            return 0
        # memoization
        if i in memo:
            return memo[i]
        # If not
        memo[i] = min(minimumCost(i-1) + cost[i-1], minimumCost[i-2] + cost[i-2])

        return memo[i]


    memo = {}
    return minimumCost(len(cost))




