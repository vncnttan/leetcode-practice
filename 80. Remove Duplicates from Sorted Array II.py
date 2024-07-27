def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if(len(nums) == 0):
        return nums
    
    j = 1

    for i in range(1, len(nums)):
        if j == 1 or nums[i] != nums[j-2]:
            nums[j] = nums[i]
            j += 1

    return j

nums = [1,1,1,2,2,3]
k = removeDuplicates(nums)
print(nums, k)