# def maxArea(height: list[int]) -> int:
    
#     maxWater = -1
#     for i in range(len(height)-1):
#         for j in range(i+1,len(height)):
#             currWater = abs(i-j) * min(height[i], height[j])
#             maxWater = max(currWater, maxWater)
    
#     return maxWater

def maxArea(height: list[int]) -> int:
    maxWater = 0
    i, j = 0, len(height) - 1
    while i < j:
        curr = abs(i-j) * min(height[i], height[j])
        maxWater = max(curr, maxWater)

        if height[i] < height[j]:
            i += 1
        else:
            j -= 1

    print(maxWater)
    return maxWater 

maxArea([1,8,6,2,5,4,8,3,7])
