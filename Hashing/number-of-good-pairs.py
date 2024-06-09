# 1512

from collections import defaultdict

def numIdenticalPairs(nums: list[int]) -> int:
    """
    Time complexity: O(n) because we iterate through all values of the array(every operation taking place inside runs in constant time)
    Space complexity: O(n) - in the case where all values in the array are unique the hashmap stores `n` key/value pairs in total
    """
    # Apparently brute force is more optimal

    pairs = defaultdict(list) # this dictionary will map values to a list consisting of which indices in the array they were seen
    res = 0 # this will keep track of number of good pairs
    for i, val in enumerate(nums):
        # the idea behind this is that if we've already encountered this value before then we can pair this value with how many ever indices are associated with the same already
        if val in pairs:
            res += len(pairs[val])
        pairs[val].append(i) # we update the list with the index it is seen at
    
    return res

print(numIdenticalPairs([1, 2, 3, 1, 1, 3]))
print(numIdenticalPairs([1,1,1,1]))
print(numIdenticalPairs([1,2,3]))