# 3095

import sys

def minimumSubarrayLength(nums: list[int], k: int) -> int:
    res = sys.maxsize

    # Brute force solutions

    # 1: 83ms runtime

    # for i in range(len(nums)):
    #     if nums[i] >= k:
    #         res = min(res, 1)
    #     for j in range(i + 1, len(nums)):
    #         or_result = 0
    #         curr = nums[i:j+1]
    #         for num in curr:
    #             or_result |= num
    #         if or_result >= k:
    #             res = min(res, j - i + 1)

    # 2: 73ms runtime

    # subarrays = []
    # for i in range(len(nums)):
    #     subarrays.append([nums[i]])
    #     for j in range(i + 1, len(nums)):
    #         subarrays.append(nums[i:j+1])
        
    # for arr in subarrays:
    #     curr = 0
    #     for elem in arr:
    #         curr |= elem
    #     if curr >= k:
    #         res = min(res, len(arr))

    # 3: 51ms runtime(Most optimal)

    for i in range(len(nums)):
        if nums[i] >= k:
            res = min(res, 1)
        curr = nums[i]
        for j in range(i + 1, len(nums)):
            curr |= nums[j]
            if curr >= k:
                res = min(res, j - i + 1)
    
    return res if res != sys.maxsize else -1

print(minimumSubarrayLength([1, 2, 3], 2))
print(minimumSubarrayLength([2, 1, 8], 10))
print(minimumSubarrayLength([1, 2], 0))