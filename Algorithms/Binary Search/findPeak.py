def findPeakElement(nums: list[int]) -> int:
    
    low, high = 0, len(nums)-1

    def binarySearch(nums: list[int],low, high) -> int:
        if low==high:
            return low
        mid = (low+high)//2
        if nums[mid] > nums[mid+1]:
            return binarySearch(nums, low, mid)
        return binarySearch(nums, mid+1, high)
    
    binarySearch(nums, low, high)

findPeakElement([1,2,1,3,5,6,4])