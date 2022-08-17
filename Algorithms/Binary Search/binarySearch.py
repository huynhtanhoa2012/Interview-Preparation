def search(nums: list[int], target: int) -> int:

    def binarySearch(nums: list[int], low, high, target):
        # when target is not exist:
        if low > high:
            print(-1)
            return -1

        mid = (low+high)//2
        # Base case
        if nums[mid] == target:
            print(mid)
            return mid
        # Recursive case
        elif nums[mid] < target:
            return binarySearch(nums, mid+1, high, target)
        else:
            return binarySearch(nums, low, mid-1, target)

    binarySearch(nums, 0, len(nums)-1, target)

search([-1,0,3,5,9,12], 2)