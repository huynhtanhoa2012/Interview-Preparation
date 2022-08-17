def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    output = []

    for i in range(len(nums)-1):
        if (i==0 or (i>0 and nums[i]!= nums[i-1])):
            low = i+1
            high = len(nums) - 1
            sum1 = 0 - nums[i]
            while low < high:
                if nums[low]+nums[high] == sum1:
                    output.append([nums[i], nums[low], nums[high]])
                    # Avoid duplicate values
                    while (low < high and nums[low] == nums[low+1]):
                        low += 1
                    while (low < high and nums[high] == nums[high-1]):
                        high -= 1
                    # Shift to another low and high
                    low += 1
                    high -= 1
                elif nums[low]+nums[high] > sum1:
                    high -= 1
                else:
                    low += 1
    return output

threeSum([-1,0,1,2,-1,-4])

        