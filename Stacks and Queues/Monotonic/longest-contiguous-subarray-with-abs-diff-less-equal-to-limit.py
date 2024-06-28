# 1438

from itertools import combinations
from collections import deque

def brute_force(nums: list[int], limit: int) -> int:
    # TLE
    
    max_len = 0
    for i in range(len(nums)):
        max_len = max(max_len, 1)
        for j in range(i + 1, len(nums)):
            curr = nums[i:j+1]
            if max(curr) - min(curr) <= limit:
                max_len = max(max_len, len(curr))

            # all the logic below is not needed because we can just check difference between maximum and min element and whether it is <= k

            # pairs = list(combinations(curr, 2))
            # counter = 0
            # for x, y in pairs:
            #     if abs(x - y) <= limit:
            #         counter += 1
            
            # if counter == len(pairs):
            #     max_len = max(max_len, len(curr))
    
    return max_len

def longestSubarray(nums: list[int], limit: int) -> int:
    """
    Time complexity: O(n) amortized because the inner while loops average out to O(1) across all iterations of the outer for loop
    Space complexity: O(n) to store both the queues
    COME BACK TO THIS AGAIN
    """

    # approach
        # KEY IDEA: WE NEED TO FIND A SUBARRAY SUCH THAT MAX(SUBARRAY) - MIN(SUBARRAY) <= LIMIT
        # WHEN THIS CONSTRAINT IS BROKEN, WE NEED TO UPDATE THE SUBARRAYS ACCORDINGLY
        # use one monotonically increasing queue to maintain min element in the current window and one monotically decreasing queue to maintain max element in the current window
    
    increasing = deque() # a monotonically increasing queue that stores the smallest element in the current window
    decreasing = deque() # monotically decreasing queue that stores the largest element in the current window
    # left pointer for the sliding window that will be used to shrink the window when the condition is violated
    l = res = 0
    for r in range(len(nums)):
        # before we can add to the monotically increasing queue, we need to make sure the element we're about to add is greater than the last element and if not we keep deleting elements from the end until we are able to maintain that property again
        while increasing and nums[r] < increasing[-1]:
            increasing.pop()
        # before we can add to the monotically decreasing queue, we need to make sure the element we're about to add is smaller than the last element and if not we keep deleting elements from the end until we are able to maintain that property again
        while decreasing and nums[r] > decreasing[-1]:
            decreasing.pop()
        
        # now that we have deleted all the necessary elements to preserve the queues properties we can add the current element to both of them
        increasing.append(nums[r])
        decreasing.append(nums[r])

        # key here is to realize that a window is invalid if the difference between its greatest and least element is greater than limit and we know that the monotonically decreasing queue has this window's greatest element at the first index and the monotonically increasing queue has this window's least element at the first index
        # we need to loop as long as the condition is violated and accordingly shrink the window until it no longer is

        while decreasing[0] - increasing[0] > limit:
            # we need the conditions below because at a given point there's no knowing at which element the left pointer is at and the neat thing is that the removal from the queues takes place in O(1) time
            if nums[l] == decreasing[0]:
                decreasing.popleft()
            if nums[l] == increasing[0]:
                increasing.popleft()
            l += 1 # actually shrinking the window

        # the current window size is right - left + 1 so we update our answer with that
        res = max(res, r - l + 1)
    
    return res


print(longestSubarray([8,2,4,7], 4))
print(longestSubarray([10,1,2,4,7,2], 5))
print(longestSubarray([4,2,2,2,4,4,2,2], 0))