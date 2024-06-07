# 217

from collections import Counter

def containsDuplicate(nums: list[int]) -> bool:
    """
    Time complexity: O(n) because in the worst case we iterate through everything in `nums` and don't find a single duplicate value
    Space complexity: O(n) because in the worst case where `nums` only has unique values then all are added to the set
    """
    
    # Approach 1(Set) - Efficient

    # if a value has already been seen in the set before then we know we have atleast one pair of duplicate values
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    
    return False

    # Approach 2(Hashmap) - Least efficient
        # if the frequency of any one given element is > 1 then we have our answer

    # freq = Counter(nums)
    # for v in freq.values():
    #     if v > 1:
    #         return True
    # return False
    
    # Approach 3(One-Liner) - Most efficient
        # if there are duplicates then the length of the array converted to a set will be less than len(arr)

    # return len(set(nums)) != len(nums)

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))