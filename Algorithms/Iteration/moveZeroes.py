def moveZeroes(nums: list[int]) -> None:

    # create a variable to store position of zero pointer
    slow = 0
    # loop through array of nums
    for i in range(len(nums) - 1):
        if nums[i] != 0:
            # swap position of current element to position of zero pointer 
            nums[i], nums[slow] = nums[slow], nums[i]
            # update zero pointer
            slow += 1
