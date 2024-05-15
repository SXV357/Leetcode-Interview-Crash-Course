# APPROACHES INVOLVING A SINGLE ITERABLE

def check_if_palindrome(s: str) -> bool:
    """
    Time complexity: O(n) - The while loop can iterate n times at most since the pointers start at distance of n. Work done inside the while loop is O(1) since only comparisons and variable updates are being done maintaining the overall complexity.
    Space complexity: O(1) - Always using only 2 pointer variables no matter what the input is(Start and end of input)
    """
    # initialize a pointer to start at the leftmost index and one at the rightmost index
    left, right = 0, len(s) - 1
    while left < right:
        # a palindrome reads the same forward and backward so at each iteration check whether the
        # characters at both indices are the same
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            # there's a mismatch and it cannot be a palindrome so return false
            return False
    # at this point, the corresponding characters at both indices are equal and both the pointers 
    # have crossed each other so the string must be a palindrome
    return True

def two_sum_modified(nums: list[int], target: int) -> bool:
    left, right = 0, len(nums) - 1 # initializing both the pointers as usual
    """
    Key: The array is sorted now so we can perform a modified binary search
    Time complexity: O(n) - the while loop iterates n times at most and all operations taking place inside the while loop are all constant(arithmetic operation + comparison) 
    Space complexity: O(1) - Still using only two pointers to handle this problem with no additional memory
    """
    while left < right:
        curr_sum = nums[left] + nums[right]
        # if the sum of elements at both the indices is less than the actual one, the leftmost element being added to the rightmost element is too small to contribute to the sum so we increment the left pointer to go to the next bigger element
        if curr_sum < target:
            left += 1
        # if the sum of elements at both the indices is greater than the actual one, the rightmost element being added to the leftmost element is too big to contribute to the sum so we decrement the right pointer to go to the previous smaller element
        elif curr_sum > target:
            right -= 1
        # we have now found two elements which when added together sum to target so return True
        else:
            return True
    # iterated through the entire array until the pointers crossed and didn't find any elements at all so the two pairs of elements don't exist
    return False

# APPROACHES INVOLVING MORE THAN ONE ITERABLE AS PART OF THE INPUTs