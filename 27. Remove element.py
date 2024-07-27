def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    count = 0
    for idx in range(len(nums)):
        nums[idx-count] = nums[idx]

        if nums[idx] == val:
            count += 1
            print(idx)

    return len(nums) - count

nums = [0,1,2,2,3,0,4,2]
val = 2
k = removeElement(nums, val)
print(nums, k)