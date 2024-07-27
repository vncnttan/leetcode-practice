def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    
    newNums = []
    numLengths = len(nums)
    for i in range(numLengths):
        newNums.append(nums[(i-k) % numLengths])
    
    for i in range(len(newNums)):
        nums[i] = newNums[i]
    return 

nums = [1,2,3,4,5,6,7]
rotate(nums, 3)

print(nums)