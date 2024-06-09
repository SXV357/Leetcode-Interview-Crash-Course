# 2958

from collections import defaultdict

def maxSubarrayLength(nums: list[int], k: int) -> int:
    """
    Time complexity: O(n) - amortized run time
    Space complexity: O(n) - if all values in `nums` are unique then the hashmap stores `n` key/value pairs in total
    """
    freq = defaultdict(int) # this dictionary will keep track of the frequency of all elements within the current window
    left = res = 0 # left pointer and variable to keep track of longest good subarray
    for right in range(len(nums)):
        freq[nums[right]] += 1 # updating the frequency of this element
        # since we want the frequency of all elements in the subarray to be < k, the moment an element's frequency exceeds k we want to start a loop where we continuously update the frequencies of all elements in the subarray starting from the left pointer while incrementing it until the condition is no longer violated
        while freq[nums[right]] > k:
            freq[nums[left]] -= 1 # update frequency of element at the left pointer
            left += 1 # increment it because we have discarded the element at the previous pointer index
        res = max(res, right - left + 1) # now that we have a valid subarray we update the maximum length
    
    return res

print(maxSubarrayLength([1,2,3,1,2,3,1,2], 2))
print(maxSubarrayLength([1,2,1,2,1,2,1,2], 1))
print(maxSubarrayLength([5,5,5,5,5,5,5], 4))