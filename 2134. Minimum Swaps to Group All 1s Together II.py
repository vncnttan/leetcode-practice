def minSwaps(nums):
    n = len(nums)
    total_ones = sum(nums)

    if total_ones == 0 or total_ones == n:
        return 0

    sliding_window = sum(nums[:total_ones])
    max_sliding_window = sliding_window

    for i in range(n):
        sliding_window -= nums[i]
        sliding_window += nums[(i + total_ones) % n]
        max_sliding_window = max(max_sliding_window, sliding_window)
    return total_ones - max_sliding_window 

nums = [1]
res = minSwaps(nums)
print(res)