def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    num_dict = {}
    requiredLength = len(nums)/2
    print(f"Req Length {requiredLength}")
    for n in nums:
        if n not in num_dict.keys():
            num_dict[n] = 0

        num_dict[n] += 1
        if num_dict[n] > requiredLength:
            return n
    return 0

nums = [3,2,3]
mj = majorityElement(nums)
print(mj)