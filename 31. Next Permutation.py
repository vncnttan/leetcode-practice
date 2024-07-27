def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    j = len(nums)-1
    switched = False

    def swap(arr, a, b):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
    
    while j >= 0 and not switched:
        # Search for greater number than immediately before
        if nums[j] > nums[j-1]:
            switched = True

            immediate_bigger = nums[j]
            immediate_bigger_idx = j

            for a_idx in range(j+1, len(nums)):
                if nums[a_idx] > nums[j-1] and nums[a_idx] < immediate_bigger:
                    immediate_bigger = nums[a_idx]
                    immediate_bigger_idx = a_idx

            # print(f"Immediate Bigger: {immediate_bigger}, immediate_bigger_idx: {a_idx + j}, j-1: {j-1}")
            # Swap j-1 with immediate bigger
            swap(nums, j-1, immediate_bigger_idx)

            # Sort the remaining from j to akhir
            for idx1 in range(j, len(nums)):
                for idx2 in range(idx1, len(nums)):
                    if nums[idx1] > nums[idx2]:
                        swap(nums, idx1, idx2)

        j -= 1

    # print(switched, nums)

nextPermutation([1,3,2])