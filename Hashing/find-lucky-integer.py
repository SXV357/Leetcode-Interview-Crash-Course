# 1394

from collections import Counter

def findLucky(arr: list[int]) -> int:
    """
    Time complexity: O(n) to find element frequencies and to iterate over all `n` key-value pairs in the worst case
    Space complexity: O(n) to store the `n` key/value pairs
    """
    freq = Counter(arr) # to store frequencies of all items in the array
    res = -1 # will store largest element whose frequency equals its value
    for k, v in freq.items():
        # if this element's frequency equals itself then we update the variable with the current maximum
        if k == v:
            res = max(res, k)
    
    return res # if the condition was never satisfied the variable would never be updated and we return -1

print(findLucky([2,2,3,4]))
print(findLucky([1,2,2,3,3,3]))
print(findLucky([2,2,2,3,3]))