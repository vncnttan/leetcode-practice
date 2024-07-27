def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    currNum = nums[0]
    count = 1
    for i in range(len(nums)):
        if nums[i] != currNum:
            currNum = nums[i]
            nums[count] = nums[i]
            count += 1

    
    return count

nums = [1,1,2]
k = removeDuplicates(nums)
print(nums, k)