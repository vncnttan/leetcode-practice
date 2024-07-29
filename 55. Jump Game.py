def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    target_idx = len(nums)
    if target_idx == 1:
        return True

    curr_idx = 0
    max_step_idx = 0

    while True:
        curr_step = nums[curr_idx]
        max_farthest_reach = nums[curr_idx] - (curr_step)
        max_step = 0

        # print(curr_idx, curr_step, max_step, target_idx)
        if curr_idx + curr_step >= target_idx-1:
            return True
        
        for i in range(curr_step+1):
            if i + curr_idx >= target_idx:
                return True

            # Searching for the max index a number can reach
            farthest_reach = nums[i + curr_idx] - (curr_step-i)
            if farthest_reach > max_step:
                max_step = nums[i + curr_idx]
                max_step_idx = i + curr_idx
                max_farthest_reach = farthest_reach
        
        
        if max_farthest_reach < 1:
            return False

        curr_idx = max_step_idx



nums = [2,0,0]
j = canJump(nums)
print(f"Result: {j}")