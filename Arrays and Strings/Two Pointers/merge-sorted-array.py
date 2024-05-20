# 88

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Time complexity: O(m + n) - indexing the respective arrays until the specified indices costs O(specified index) and the while loops combined are O(m + n)
    Space complexity: O(m + n) - storing two arrays, one storing first m elements of nums1 and the other storing the first n elements of nums2 which grow as size of m and/or n grow
    """
    # NOTE: THE BASE CASES BELOW AREN'T QUITE NECESSARY SINCE THE MAIN LOGIC ITSELF HANDLES EVERYTHING BUT GOOD TO HAVE NONETHELESS
    if m == 0 and n != 0: # if m = 0, nothing to merge from nums1 or store in it so just use n elements in nums2
        nums1[:] = nums2[:n]
    if n == 0 and m != 0: # if n = 0 then nothing to merge from nums2 hence we just use the m elements in nums1
        nums1[:] = nums1[:m]
    if m == 0 and n == 0: # nothing to merge so just set it to an empty array
        nums1[:] = []
    
    # handle case where m != 0 and n != 0

    m1, m2 = nums1[:m], nums2[:n] # store first m and n elements from nums1 and nums2 respectively so that as we're modifying nums1 in place we don't lose track of any elements
    i = j = curr_idx = 0
    # the key is that both arrays are alredy sorted so we can start two pointers at the start of both respective arrays and compare elements while updating nums1 with the right order
    while i < m and j < n:
        # m1[i] should come first in nums1 so update nums1 and move its respective pointer as well as the index to fill in the next index for the next element in nums1
        if m1[i] <= m2[j]:
            nums1[curr_idx] = m1[i]
            i += 1
            curr_idx += 1
        # m2[j] should come first so update nums1 and move its respective pointer as well as the index to correctly fill in the next element
        elif m1[i] > m2[j]:
            nums1[curr_idx] = m2[j]
            j += 1
            curr_idx += 1
    
    # at this point only one of the arrays would've been exhausted and we need to exhaust the other array as well
    
    # no comparisons need to be done since both arrays are sorted and we are adding elements to the resulting list also in increasing order
    while i < m:
        nums1[curr_idx] = m1[i]
        i += 1
        curr_idx += 1
    
    while j < n:
        nums1[curr_idx] = m2[j]
        j += 1
        curr_idx += 1
    
    print(f"Result list: {nums1}")\

merge([1,2,3,0,0,0], 3, [2, 5, 6], 3)
merge([1], 1, [], 0)
merge([0], 0, [1], 1)