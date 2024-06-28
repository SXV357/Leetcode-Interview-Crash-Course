# 239

from collections import defaultdict, deque

def approach_one(nums: list[int], k: int) -> list[int]:
    # TLE
    res = []
    res.append(max(nums[:k]))

    for i in range(1, len(nums) - k + 1):
        curr = nums[i:i+k]
        res.append(max(curr))
    
    return res

def approach_two(nums: list[int], k: int) -> list[int]:
    # TLE
    res = []
    queue = deque([], k)
        
    for i in range(len(nums)):
        queue.append(nums[i])
        if len(queue) == k:
            res.append(max(queue))
    
    return res

def approach_three(nums: list[int], k: int) -> list[int]:
    # TLE
    res = []
    if k == 1:
        return nums

    queue = deque([])
    mappings = defaultdict(lambda: [[], 0])
    for i in range(1, len(nums) - k + 1):
        mappings[nums[i]][0].append(i)
    
    curr_max = 0
    queue.append(nums[0])
    curr_max = max(curr_max, nums[0])
    i = 1
    while True:
        for _ in range(k - 1):
            queue.append(nums[i])
            curr_max = max(curr_max, nums[i])
            i += 1
        
        if i == len(nums):
            res.append(curr_max)
            break
        
        if len(queue) == k:
            res.append(curr_max)
            queue.popleft()
            while len(queue) != 1:
                queue.pop()
            curr_max = queue[0]
            last_idx = mappings[curr_max][1]
            while i != mappings[curr_max][0][last_idx] + 1:
                i -= 1
            mappings[curr_max][1] += 1
    
    return res

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    """
    Time complexity: O(n) - since all the queue operations being performed are O(1) and the inner while loop averages out to O(1) across all iterations of the main for loop the runtime is O(n) amortized
    Space complexity: O(n) to primarily store the resulting array but includes the deque as well

    COME BACK TO THIS TOMORROW TO RE-ATTEMPT
    """
    res = []

    # main idea:
        # if we use a monotonically decreasing data structure then the very first element in it will be the maximum element
        # this is like a sliding window problem where we need to keep adding elements from one end as long as they're valid and delete elements in the following scenarios
            # when the element at the top of the stack is lesser than the one we're currently looking at
            # when the very first element in the queue needs to be removed because it doesn't fall within the window size
        # since all the additions/removals need to happen optimally, we use a doubly-ended queue which makes it such that all of these happen in O(1)
        # at any given point, if we encounter an element that is greater than the element at the top of the queue we keep deleting the elements from the queue until we are back to a monotonically decreasing structure
        # since we need to maintain a fixed window of size k, we need to ensure that the bounds of the sliding window are also appropriate so if the leftmost element ever falls out of bounds we delete it
        # in other cases when we have looked at atleast k elements, the first element in the queue will be the maximum value of that given window so we can add that to our answer

    queue = deque([]) # this queue will be used to store indices of the seen numbers because it will make it easier to detect when we have visited k elements within a given window and if at all there ever is a out-of-bounds situation
    for i in range(len(nums)):
        # since we want to ensure the elements in the queue are in decreasing order, we need to keep deleting elements from the top of the queue until they meet that condition and we use the current element to determine that
        while queue and nums[i] > nums[queue[-1]]:
            queue.pop()
        
        # once we've removed all smaller elements the queue is back to decreasing order and we can add the current element while knowing that it maintains the property
        queue.append(i)

        # this is an edge case when the first element in the queue is out of bounds of the current window
        # in order to ensure we maintain the fixed window size we need to get rid of the max element of the previous window so that we can start off from the first element of this new window which may or may not end up being the maximum
        if queue[0] + k == i:
            queue.popleft()
        
        # the first time it means we have visited k elements and in all subsequent iterations we are maintaining the fixed window size anyways but at this point the first element in the queue holds the maximum value of the given window so we add that to our answer
        if i >= k - 1:
            res.append(nums[queue[0]])
    
    return res

    
print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(maxSlidingWindow([-7,-8,7,5,7,1,6,0], 4))

print(maxSlidingWindow([1], 1))
print(maxSlidingWindow([1,-1], 1))