# 3095

import sys

def minimumSubarrayLength(nums: list[int], k: int) -> int:
    res = sys.maxsize
    left = curr = 0
    for right in range(len(nums)):
        curr |= nums[right]
        while curr >= k:
            res = min(res, right - left + 1)
            # something to update curr here
            left += 1
    
    return res if res != sys.maxsize else -1

print(1 | 1)