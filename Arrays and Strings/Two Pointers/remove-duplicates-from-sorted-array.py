# 26

# Trivial approach:
    # Convert input array into a set, convert this set into an array and sort it
    # Return length of this modified array

def removeDuplicates(nums: list[int]) -> int:
    """
    Time complexity: O(n) - Iterate through all elements of nums in the main loop
    Space complexity: O(n) - If we include the set, it can store a max of n elements in the case that there are no duplicates otherwise O(1)
    """
    # The num_unique variable is used to store the number of unique elements in the array
    # curr_idx is used to modify nums in place starting from the beginning with only unique values
    num_unique, curr_idx = 0, 0
    seen = set() # to keep track of all visited elements as well as duplicates
    for num in nums:
        # if it doesn't exist in the set we know its a unique number
        if num not in seen: # O(1) operation
            seen.add(num)
            nums[curr_idx] = num # start modifying nums in-place from index 0 with this current unique value
            curr_idx += 1 # if there are more unique values to store that at the next index
            num_unique += 1 # found a unique element so update the count
        
    return num_unique

print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))