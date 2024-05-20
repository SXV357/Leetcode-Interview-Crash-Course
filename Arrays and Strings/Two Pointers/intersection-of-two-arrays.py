# 349

# Trivial approach:
    # convert both lists into a set and get their intersection
    # convert the intersection set back into a list and return it

def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Time complexity: O(max(n log n, m log m))
    Space complexity: O(max(n, m)) since it is possible that if n = m then all elements of n/m are added to the resulting array which would grow for large values of them respectively
    """
    # We assume len(nums1) = n and len(nums2) = m. Sorting in general happens in O(n log n) time at best
    res = [] # will store all the elements common to both arrays
    seen = set() # O(n)
    # Maybe no need to sort the arrays but in this case doing so so that we can capture all the intersecting elements
    nums1.sort() # O(n log n)
    nums2.sort() # O(m log m)

    i = j = 0
    # similar to problem regarding finding the minimum common element in two arrays except that the two arrays were already sorted
    while i < len(nums1) and j < len(nums2): # O(m + n)
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            # when we encounter a match, we need to check if it already exists in the set otherwise we will end up having duplicate elements in the result list
            if nums1[i] not in seen:
                seen.add(nums1[i])
                res.append(nums1[i])
            i += 1
            j += 1
    
    return res

print(intersection([1,2,2,1], [2, 2]))
print(intersection([4,9,5], [9,4,9,8,4]))