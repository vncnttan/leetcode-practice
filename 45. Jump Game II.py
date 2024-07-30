def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    jump_count = 0
    curr_idx = 0
    max_step_idx = 0

    targetLength = len(nums)
    
    if targetLength == 1:
        return 0

    if(nums[0] >= targetLength-1):
        return 1
    
    while True:
        curr_step = nums[curr_idx]
        max_farthest_reach = 0
        max_step = 0

        
        for i in range(curr_step+1):
            farthest_reach = nums[i + curr_idx] - (curr_step - i)
            print(f"{nums[i+curr_idx]} - ({curr_step} - {i})")
            print(f"\t{farthest_reach}")
            if farthest_reach > max_farthest_reach:
                max_farthest_reach = farthest_reach
                max_step = nums[i + curr_idx]
                max_step_idx = i + curr_idx
        print(curr_step, max_step_idx, max_farthest_reach)
        return

        if max_farthest_reach < 1:
            return 0 

        jump_count += 1
        curr_idx = max_step_idx 
        
        if nums[curr_idx] + curr_idx >= targetLength-1:
            return jump_count + 1

nums = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
j = jump(nums)
print(f"Result: {j}")