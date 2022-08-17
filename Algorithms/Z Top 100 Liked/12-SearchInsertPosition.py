def searchInsert(nums: list[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    res = -1

    while low < high:
        mid = (low + high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return low + 1 if target > nums[low] else low 

searchInsert([1,3,5,6], 7)