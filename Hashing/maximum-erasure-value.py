# 1695

from collections import defaultdict

def maximumUniqueSubarray(nums: list[int]) -> int:
    """
    THIS PROBLEM'S RUNTIME COULD'VE BEEN WORSE IF WE DIDN'T MAINTAIN A VARIABLE TO KEEP TRACK OF THE CURRENT SUBARRAY SUM OR PERHAPS DIDN'T USE A PREFIX SUM APPROACH. SINCE WE HAVE A LEFT AND RIGHT POINTER THE NAIVE APPROACH WOULD'VE BEEN MANUALLY GETTING THE SUM OF EVERYTHING BETWEEN THE POINTERS INCLUSIVE

    Time complexity: O(n) amortized run time
    Space complexity: O(n) if we need to store `n` key/value pairs in the worst case
    """
    freq = defaultdict(int) # this dictionary will store the frequencies of all elements in nums
    # res: to store the maximum score, curr: to keep track of the current valid subarray sum, left: left pointer
    res = curr = left = 0
    for right in range(len(nums)):
        freq[nums[right]] += 1 # updating the frequency of this element in the dictionary
        curr += nums[right] # updating curr with the current subarray sum
        # since a valid subarray needs to only contain unique elements the moment an element's frequency exceeds 1 we need a loop to shrink the window until the condition is no longer violated. with each shrink we do the following:
            # decrement the frequency of the leftmost element since we're deleting it
            # subtract the leftmost element from the current subarray sum once again because its being deleted
            # move the left pointer ahead to now point at the start of the current valid window
        while freq[nums[right]] > 1:
            freq[nums[left]] -= 1
            curr -= nums[left]
            left += 1
        res = max(res, curr) # at this point we have a valid subarray along with its sum so we can update res 
    
    return res

print(maximumUniqueSubarray([4,2,4,5,6]))
print(maximumUniqueSubarray([5,2,1,2,5,2,1,2,5]))