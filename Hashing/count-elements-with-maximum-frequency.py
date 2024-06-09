# 3005

def maxFrequencyElements(nums: list[int]) -> int:
    """
    Time complexity: O(n) - to update the dictionary with frequencies and then to calculate the maximum value
    Space complexity: O(n) to store the `n` key-value pairs in the dictionary in the worst case
    """
    # the logic below is for updating the dictionary with the frequency of all elements in nums
    freq = {}
    for num in nums:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
    
    res = 0 # this will store the total frequency of elements that have a frequency equal to the maximum one
    max_freq = max(freq.values()) # calculate and store the maximum frequency
    for v in freq.values():
        # if we find a frequency equal to the maximum frequency we update the result by incrementing it with that frequency
        if v == max_freq:
            res += v
    
    return res

print(maxFrequencyElements([1,2,2,3,1,4]))
print(maxFrequencyElements([1,2,3,4,5]))