# 930

from collections import defaultdict

def numSubarraysWithSum(nums: list[int], goal: int) -> int:
    """
    Time complexity: O(n) - a single pass through the array with all operations that are happening inside in constant time
    Space complexity: O(n) to store `n` key/value pairs in the dictionary in the worst case
    """
    # the idea behind this problem is to sort of use a running prefix along with a hashmap to count the number of valid subarrays
    mappings = defaultdict(int) # this dictionary will map the sum of the subarray to how many subarrays have a sum equal to that given key
    mappings[0] = 1 # only one subarray has a sum of 0 which is the empty subarray so we intialize that in the hashmap to begin with
    res = curr = 0 # res will keep track of the number of valid subarrays while curr will be used to keep a track of the current prefix sum
    for i in range(len(nums)):
        curr += nums[i] # we update curr to include the sum of the current element so far
        # the reason why we update res this way is interesting:
            # let's say the input we have is [1, 0, 1, 0, 1] with goal = 2 and the output is supposed to be 4
            # the sum after including the first element is 1 which doesn't meet 2 yet so when we update res we add 0 because the key for -1 gets added to the dictionary with a default value of 0
            # when we get to index 2 we get curr - goal = 0 and the key exists in the dictionary so we add 1 and so far we have seen one subarray with the sum of 2
            # then when we add the next element the sum is still 2 and we add 1 again to the result
            # basically what happens is that by the time we reach the end and we get a sum of 3 where curr - goal = 1 we have seen 1 in the dictionary with a value of 2 corresponding to the subarrays [1] and [1, 0] initially and the reason we add 2 is that if we delete the first two elements we are left with [1, 0, 1] which is a valid subarray
        res += mappings[curr - goal]
        mappings[curr] += 1 # we have seen one subarray so far with the current sum so we update that in the array
    
    return res

print(numSubarraysWithSum([1,0,1,0,1], 2))
print(numSubarraysWithSum([0,0,0,0,0], 0))