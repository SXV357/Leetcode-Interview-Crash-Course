# 1748

from collections import Counter

def sumOfUnique(nums: list[int]) -> int:
    """
    Time complexity: O(n) to iterate over all `n` key value pairs in the worst case when every single value is unique
    Space complexity: O(n) to store the hashmap with `n` key-value pairs
    """
    freq = Counter(nums) # to maintain frequency of all elements in nums
    res = 0 # this will store the sum of all the unique elements
    for k, v in freq.items():
        res += k if v == 1 else 0 # this element only appears once so we add it to the sum
    
    return res

print(sumOfUnique([1,2,3,2]))
print(sumOfUnique([1,1,1,1,1]))
print(sumOfUnique([1,2,3,4,5]))