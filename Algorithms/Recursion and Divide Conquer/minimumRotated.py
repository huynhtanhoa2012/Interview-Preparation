# Iterative
def findMin(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    low, high = 0, len(nums)-1

    while low<high:
        mid = (low+high)//2
        if nums[mid] < nums[high]:
            high = mid
        else:
            low = mid + 1
    print(nums[low])
    return nums[low]

def findMinRecursive(nums: list[int]) -> int:
    
    def binarySearch(nums, low, high):
        if low == high:
            print(nums[low])
            return nums[low]
        mid = (low+high)//2
        if nums[mid] < nums[high]:
            return binarySearch(nums, low, mid)
        else:
            return binarySearch(nums, mid+1, high)
    return binarySearch(nums, 0, len(nums)-1)

findMinRecursive([3,4,5,1,2])