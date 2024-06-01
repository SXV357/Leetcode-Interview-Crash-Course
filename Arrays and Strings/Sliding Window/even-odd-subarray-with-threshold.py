# 2760

def check_conditions(arr: list[int], thresh: int) -> bool:
    """
    For the input array `arr` the following conditions are checked:
        - The element at the leftmost index is divisible by 2, i.e., `arr[0] % 2 == 0`
        - For all indices `i` in the range `[l, r - 1]`, `arr[i] % 2 != arr[i + 1] % 2`
        - For all indices `i` in the range `[l, r]`, `arr[i] <= threshold`
    
    Time Complexity: O(l - r) since `len(arr) = l - r + 1` and the first loop is running `l - r` times with the second loop runing `l - r + 1` times which without taking into account constants yields a runtime of the above
    Space Complexity: O(1) - Just using a single boolean variable that holds the result of all the checked conditions
    """

    # Check 1: The element at the leftmost index is divisible by 2
    if arr[0] % 2 != 0:
        return False
    
    # Check 2: All elements are alternating in their divisibility by 2
    for x in range(len(arr) - 1):
        if arr[x] % 2 == arr[x + 1] % 2:
            return False
    
    # Check 3: All elements are less then or equal to the threshold
    for y in range(len(arr)):
        if arr[y] > thresh:
            return False
    
    return True

# attempt at recursive approach

# def alternatingSubarrayHelper(l, r, nums, threshold):
#     if l > len(nums) - 1:
#         return 0
    
#     if nums[l] % 2 != 0 or nums[l] > threshold:
#         return alternatingSubarrayHelper(l + 1, r, nums, threshold)
#     else:
#         if check_conditions(nums[l:r+1], threshold):
#             return r - l + 1
#         else:
#             return max(alternatingSubarrayHelper(l + 1, r, nums, threshold), alternatingSubarrayHelper(l, r - 1, nums, threshold))

def longestAlternatingSubarray(nums: list[int], threshold: int) -> int:
    """
    The constraints are relatively small so brute force solution works. Would need to consider optimization for larger input sizes
    """
    # Brute force approach

    max_len = 0
    for i in range(len(nums)):
        if check_conditions([nums[i]], threshold):
            max_len = max(max_len, 1)
        for j in range(i + 1, len(nums)):
            curr = nums[i:j+1]
            if check_conditions(curr, threshold):
                max_len = max(max_len, len(curr))
    
    return max_len

    # Attempt at 2-pointers approach

    # l, r, res = 0, len(nums) - 1, 0
    # while True:        
    #     if nums[l] % 2 != 0 or nums[l] > threshold:
    #         l += 1
    #     else:
    #         if check_conditions(nums[l:r + 1], threshold):
    #             res = max(res, r - l + 1)
    #             break
    #         else:
    #             first, second = check_conditions(nums[l + 1:r + 1], threshold), check_conditions(nums[l:r], threshold)
    #             first_bound, second_bound = l + 1, r - 1
    #             if first:
    #                 res = max(res, r - first_bound + 1)
    #                 break
    #             elif second:
    #                 res = max(res, second_bound - l + 1)
    #                 break
    #             elif first and second:
    #                 res = max(res, max(r - first_bound + 1, second_bound - l + 1))
    #                 break
                    
    #             # if check_conditions(nums[l + 1:r + 1], threshold):
    #             #     new = l + 1
    #             #     res = max(res, r - new + 1)
    #             #     break
    #             # r -= 1
    
    # return res

print(longestAlternatingSubarray([3, 2, 5, 4], 5))
print(longestAlternatingSubarray([1, 2], 2))
print(longestAlternatingSubarray([2, 3, 4, 5], 4))
print(longestAlternatingSubarray([2, 2], 18))