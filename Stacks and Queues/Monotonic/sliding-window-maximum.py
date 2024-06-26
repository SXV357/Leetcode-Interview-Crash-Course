# 239

from collections import deque
# import sys

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    res = []
    # res.append(max(nums[:k]))

    # for i in range(1, len(nums) - k + 1):
    #     curr = nums[i:i+k]
    #     res.append(max(curr))

    # for i in range(len(nums)):
    #     queue.append(nums[i])
    #     if len(queue) == k:
    #         res.append(max(queue))

    if k == 1:
        return nums

    queue = deque([], k)
    curr_max =  0
    for i in range(len(nums)):
        queue.append(nums[i])
        if nums[i] > curr_max:
            curr_max = nums[i]
        if len(queue) == k:
            print(f"Queue: {queue}")
            print(f"Curr max: {curr_max}")
            res.append(curr_max)
            curr_max = queue[1]
            print(f"new max: {curr_max}")
    
    return res

print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(maxSlidingWindow([1], 1))
print(maxSlidingWindow([1,-1], 1))