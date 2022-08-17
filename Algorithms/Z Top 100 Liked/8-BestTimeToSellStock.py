def maxProfit(prices: list[int]) -> int:
    maxProfit = 0
    minVal = float('inf')

    for i in range(len(prices)):
        # check if price at index i is minimum value
        if prices[i] < minVal:
            minVal = prices[i]
        # if price at index i is bigger update profit
        elif prices[i] - minVal > maxProfit:
            maxProfit = prices[i] - minVal

    return maxProfit



maxProfit([7,1,5,3,6,4])