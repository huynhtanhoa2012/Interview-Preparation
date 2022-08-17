def trap(height: list[int]) -> int:
    left = [0]*len(height)
    right = [0]*len(height)

    # Find left and right max height per i
    max_left = 0
    max_right = 0
    for i in range(1, len(height)):
        max_left = max(max_left, height[i-1])
        left[i] = max_left
    for i in range(len(height) - 2, -1, -1):
        max_right = max(max_right, height[i+1])
        right[i] = max_right
    
    water = 0
    # Calculate water
    for i in range(len(height)):
        current = min(left[i], right[i]) - height[i]
        if current > 0:
            water += current
    return water


height = [0,1,0,2,1,0,1,3,2,1,2,1]
trap(height)