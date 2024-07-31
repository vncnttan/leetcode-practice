def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    numLen = len(nums)
    leftArr = [1 for _ in range(numLen )]
    rightArr = [1 for _ in range(numLen)]
    
    # Calculate left product
    for i in range(1, numLen):
        leftArr[i] = leftArr[i-1] * nums[i-1]

    for i in range(numLen-2, -1, -1):
        rightArr[i] = rightArr[i+1] * nums[i+1]

    arrayResult = []
    for i in range(numLen):
        arrayResult.append(leftArr[i] * rightArr[i])

    return arrayResult

nums = [1,2,3,4]
res = productExceptSelf(nums)
print(res)