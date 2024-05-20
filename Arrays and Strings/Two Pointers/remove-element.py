# 27

def removeElement(nums: list[int], val: int) -> int:
    """
    Time complexity: O(n) - always iterate through every single value in the input array
    Space complexity: O(1) - just using 2 variables to keep track of number of non-match elements as well as for modifying the list in-place
    """
    # remaining is to keep track of number of elements in nums which are not equal to val
    # curr_idx is for modifying the list with non-matched elements from the beginning 
    remaining, curr_idx = 0, 0
    for num in nums:
        if num != val: # we have found a value which is not equal to val
            nums[curr_idx] = num # update the array starting from index 0 with this non-matched value
            curr_idx += 1 # increment the index so that the next time we find another non-matched value we can update the array at the new index
            remaining += 1 # update count to reflect number of matched elements

    return remaining

print(removeElement([3,2,2,3], 3))
print(removeElement([0,1,2,2,3,0,4,2], 2))