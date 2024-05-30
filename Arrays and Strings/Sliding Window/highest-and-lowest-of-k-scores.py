# 1984

# import itertools
import sys

def minimumDifference(nums: list[int], k: int) -> int:
    """
    How would sliding window be implemented here if there's scope for doing so?
    """
    if k > len(nums) or len(nums) == 1:
        return 0
    if k == len(nums):
        return max(nums) - min(nums)

    res = sys.maxsize
    
    # Brute force 1: Pick all possible sets of scores of k students and calculate the minimum difference between them

    # TC: O(n!/k! * (n - k)!) since this is how many k-combinations exist in a list of size n
    # SC: Memory limit exceeded since as the size of the input array grows the number of combinations also increases
    
    # combinations = list(itertools.combinations(nums, k))
    # for i in range(len(combinations)):
    #     res = min(res, max(combinations[i]) - min(combinations[i]))
    
    # return res

    # Brute force 2: Sort the input array so that the difference between pairs of k elements are minimized and instead of picking all possible pairs of k elements, only taking into account subarray pairs instead of subsequence pairs of well. There's no need to consider subsequence k-pairs since sorting it gives for a small difference

    # TC: O(nlogn) - All operations inside the loop happen in linear time but the sorting dominates everything
    # SC: O(1) since no extra space is being used or data structures that scale with input size

    nums.sort() # O(n log n)
    for i in range(len(nums) - k + 1): # O(n - k + 1)
        curr = nums[i:i+k] # O(k)
        # since the array is already sorted, if we want to find the difference between the greatest and the least element then we can simply take the difference of the last element and the first element since in this subarray of k elements it will be sorted
        res = min(res, curr[-1] - curr[0]) # O(1)
        # res = min(res, max(curr) - min(curr))
    
    return res

print(minimumDifference([90], 1))
print(minimumDifference([9, 4, 1, 7], 2))
    