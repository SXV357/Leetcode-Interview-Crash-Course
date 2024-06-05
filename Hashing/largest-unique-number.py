# 1133

from collections import Counter

def largestUniqueNumber(nums: list[int]) -> int:
    """
    Time complexity: O(n) since if freq has `n` keys where `len(nums) = n` then we iterate `n` times
    Space complexity: O(n) since in the case where all values in the array are unique the hashmap stores `n` keys
    """

    freq = Counter(nums) # store frequency of values
    res = -1 # this will store the maximum value that appears only once
    for k in freq.keys():
        if freq[k] == 1: # check if this value appears once and only then perform the calculation
            res = max(res, k) # if we never encounter a key that appears only once then res will never be updated
    
    return res

print(largestUniqueNumber([5,7,3,9,4,9,8,3,1]))
print(largestUniqueNumber([9,9,8,8]))