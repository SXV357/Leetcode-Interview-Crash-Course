# General idea
    # Right pointer can move a max of "n" times and left pointer can move a max of "n" times so 2n iterations guaranteed at best
    # overall time complexity is O(n) despite having a while loop inside the for loop because the while loop can only execute a max of n times

# DYNAMIC WINDOW SIZES

def sum_less_than_k(nums: list[int], k: int) -> int:
    """
    Time complexity: O(n) - The outer loop runs a max of "n" times and the inner loop can also run a max of "n" times but it is limiting for purposes of the 
    problem. Each element in the array is processed at most once by the inner loop and this processing is O(1) so it balances out and results in an overall complexity of O(n)
    - Above is the amortized complexity of the algorithm but if we consider worst case complexity it is O(n^2)
    Space complexity: O(1) - Only three integer variables used and no use of additional data structures that grow with input size
    """
    # Metric constraint: sum
    # Numeric constraint: k
    left = 0
    curr = 0
    res = 0
    # right pointer is used to expand the window
    for right in range(len(nums)):
        curr += nums[right] # this is used to maintain the current sum(i.e the sum of the current subarray)
        # This is the part where we check if the subarray violates the condition specified in the problem(i.e the sum of the subarray exceeding k)
        while curr > k:
            # We want to make the subarray valid so we delete elements from the left to make it valid while also updating the left pointer.
            # In this way, we are only considering valid subarrays throughout the entire algorithm
            curr -= nums[left]
            left += 1
        # right - left + 1 is the length of the subarray starting at the leftmost index(left) and ending at the rightmost index(right)
        # this logic is used to update the length of the longest subarray
        res = max(res, right - left + 1)
    
    # The algorithm keeps expanding the subarray to the right until the sum exceeds k then it runs a while loop to shrink the current subarray
    # by deleting elements from it until the subarray becomes valid again and then updates the maximum length
    
    return res

def flip_binary(s: str) -> int:
    """
    What is the length of the longest substring achievable that contains only "1"?
    Time complexity: O(n) - Amortized since we're averaging out runtime of inner loop across all iterations
    Space complexity: O(1) - No additional data structures used that grow with input size and only 3 variables used
    """
    # metric constraint: length, numeric constraint: contain only 1's
    # can interpret the problem as asking what the length of the longest substring is that contains a max of 1 zero
    # hence, the violating condition would be when we have more than one "0" in the window at which point we shrink it
    left = res = count = 0
    for right in range(len(s)):
        # if we encounter a zero in the string we update the count of the number of zero's and keep moving right
        if s[right] == "0":
            count += 1
        # this is where the condition is broken and we shrink the window iteratively until we have a valid window
        while count > 1:
            # checking if the element at the left pointer is a zero since we are working with the count of zero's and 
            # simply updating the value of count without this check won't work
            if s[left] == "0":
                count -= 1
            # shrinking the window
            left += 1
        res = max(res, right - left + 1) # updating the length of the longest window as per the problem statement
    return res

def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
    """
    Time complexity: O(n) - Check for >= in the beginning base case and amortized run time of while loop wrt the main loop
    Space complexity: O(1) - No extra memory being used apart from the 3 variables used
    """
    # we know that all values in the array have a range of [1, 1000] and we are finding all subarrays with product < k
    # however, this can never be the case with all values of k <= 1 since no subarrays will fit that constraint(all products will always either be >= k and never less than k)
    if k == 0 or all(i >= k for i in nums):
        # can simply do (if k <= 1: return 0)
        return 0

    left = res = 0
    curr = 1 # cannot have it zero since we're calculating product
    for right in range(len(nums)):
        curr *= nums[right] # accumulating product as we're expanding the window
        while curr >= k: # condition has been violated here and we want to keep shrinking window until the window is valid
            curr //= nums[left] # update curr to remove elements that make window valid
            left += 1 # actually shrinking the window
        
        # this is a neat trick to use for calculating number of subarrays since the number of subarrays between 2 indices is given by: (right - left + 1)
            # example: [1, 2, 3] and right = 2, left = 0
            # here we have 3 valid subarrays which are [1, 2, 3], [2, 3], [3] since we can fix the right pointer and the left pointer can take on the following values:
                # left = 0, left = 1, left = 2 which are all values starting at the original point until the position of the right pointer
        res += (right - left + 1)
    
    return res

# FIXED WINDOW SIZES

# Intuition:
    # Build the initial window from 0 -> k - 1 with whatever condition has been specified
    # Then constantly update the window to maintain the fixed size by including an element on the right and deleting an element on the left

def largest_sum(arr: list[int], k: int) -> int:
    """
    Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k
    Time complexity: O(n) - O(k) for the first loop and O(n - k) for the second loop
    Space complexity: O(1) - Only using an extra variable to keep track of current window sum beyond the one for the first k elements
    """
    # we first accumulate the sum of the first k elements so that we have it as a reference point to use in future calculations
    res = sum(arr[:k]) # O(k) since we're iterating over the first k elements and getting the sum
    curr = res # this variable is used to perform future updates and to accordingly update the largets sum

    # O(n - k) since we're iterating those many times
    for i in range(k, len(arr)): # we start at k and we move in windows of size k along the rest of the array
        curr += (arr[i] - arr[i - k]) # we have already gotten the sum of the first k elements and we want to only consider windows of size k
        # since we're adding one element on the right and deleting one element on the left we're always looking at windows only of the specific size
        res = max(res, curr) # as we're updating curr to now hold the sum of the elements in the new window, we need to also update the original sum to hold the current maximum value
    
    return res

def findMaxAverage(nums: list[int], k: int) -> float:
    """
    Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value
    Time complexity: O(n) - O(k) for the initial sum calculation + O(n - k) for the running loop
    Space complexity: O(1) - No extra memory being used that is directly proportional to input size but just 3 variables
    """
    initial_sum = sum(nums[:k]) # accumulating sum of first k elements in the array
    res = initial_sum / k # calculating average of first k elements
    curr = initial_sum # this variable will be used to keep track of the running sum of all windows of size k after the initial k elements

    for i in range(k, len(nums)):
        curr += (nums[i] - nums[i - k]) # move in windows of size k adding the next element and discarding the left element to maintain that fixed size
        res = max(res, curr / k) # now that we have the updated sum of the next window of size k, we can accordingly update the maximum average
    
    return res

def longestOnes(nums: list[int], k: int) -> int:
    """
    Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's
    Time complexity: O(n) - Amortized run time of entire algorithm
    Space complexity: O(1) - 3 variables used and no additional memory dependent on input size
    """

    # Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
    # Output: 6
    # Explanation: [1,1,1,0,0,1,1,1,1,1,1]
    #                         _ _ _ _ _ _
    # Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

    # Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
    # Output: 10
    # Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
    #                   _ _ _ _ _ _ _ _ _ _
    # Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

    # Maximum length of a substring containing only 1's with a max of k zero's
        # Keep moving right along the string until the current window becomes invalid(> k 0's) and in that case keep deleting 0's until we have only k 0's
    
    # Exact same as the flip_binary problem except that now we are allowed to flip a max of k zero's instead of just 1 zero
    # the idea here is that we want to find the length of the longest substring containing a max of k zero's because those k zero's can be flipped to 1's to achieve a substring of only one's
    left = curr = ans = 0
    for right in range(len(nums)):
        # count the number of zero's because we want to keep track of how many zero's exist in the current substring
        if nums[right] == 0:
            curr += 1
        # the condition has been broken where we have > k zero's so we need to keep deleting 0's from the left and shrinking the window until it is valid once again
        while curr > k:
            if nums[left] == 0:
                curr -= 1
            left += 1
        # updating the length of the longest window
        ans = max(ans, right - left + 1)
    
    return ans

import sys

def minSubArrayLen(target: int, nums: list[int]) -> int:
    """
    ** Come back to this problem later **
    Time complexity: O(n) - Amortized run time
    Space complexity: O(1) - Only 3 variables used and no additional data structures that grow with input size
    """
    # Intuition for the problem:
        # We want to keep adding elements to the current sum as long as it is less than the target
        # After the sum exceeds target for the first time, we have found the first smallest subarray whose sum is >= k and we can update the length accordingly
        # Key is that the updating of the minimum length has to happen within the while loop instead of outside the while loop
    
    # Problem with the below approach is that while all the calculations are happening correctly, the updating of the minimum subarray length is not happening properly
    # As we're removing elements to make the sum < target, we are not considering all the intermediate subarrays as well that could possibly satisfy the condition
    # Updating the length only when the while loop is done results in not considering all smaller subarrays within the initial matches that work
    # FIX: MOVE THE MIN LENGTH UPDATE LOGIC INSIDE THE WHILE LOOP. WHY?
        # let's say with the example [2, 3, 1, 2, 4, 3]
        # we expand until we get [2, 3, 1, 2] and for now the length of the smallest array that satisfies the condition is 4
        # we delete 2 and end up with [3, 1, 2] but this doesn't satisfy the condition again so we add another element
        # now we get [3, 1, 2, 4] with a sum of 10 with the length being 4. now we remove 3 and still have 7 >= 7, meaning that we have found an
            # intermediate subarray which is [1, 2, 4] of length 3 with sum of 7 that satisfies the condition
        # this process continues until we get to the end where we have [4, 3] and update the length to get 2, after which the pointers equal one another and the loop terminates

    # Reverse logic from problems involving "largest subarray with sum < k":
        # keep adding elements, while sum >= k, keep deleting elements and after while loop update length
    # For this problem we are deleting elements from the left to make the window invalid rather than valid so that we can accordingly update the minimum length(major difference)
    
    left = curr = 0
    res = sys.maxsize # store the largest possible value but length of the array also works since the minimum length of a subarray could span the whole array itself
    for right in range(len(nums)):
        curr += nums[right] # keep adding elements to the current sum
        while curr >= target: # we have found the first subarray with sum >= k
            res = min(res, right - left + 1) # right away update the length variable to store this given length. while deleting elements from the left
                                             # if we end up with more subarrays that still have sum >= k causing another deletion, we have found another subarray satisfying the condition
            curr -= nums[left]
            left += 1
        # res = min(res, right - left + 1) this doesn't go here(incorrect update)
        
    return res if res != sys.maxsize else 0 # if the sum of all values is < target then res never gets updated so we can return 0 right away or in any other corner case

def maxVowels(s: str, k: int) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(1) - Only 2 variables being used which take up constant space
    """
    vowels = {"a", "e", "i", "o", "u"} # set lookups take place in O(1)
    res = 0
    # first calculating number of vowels in first "k" characters of s
    for i in range(k): # O(k)
        if s[i] in vowels: # O(1)
            res += 1
    curr = res # this will be used to keep track of number of vowels in ongoing substrings of size k in s
    for j in range(k, len(s)): # O(n - k)
        # if the incoming character is a vowel, we increment the counter
        if s[j] in vowels: # O(1)
            curr += 1
        # if the leftmost character to be deleted was a vowel, we decrement the counter
        if s[j - k] in vowels: # O(1)
            curr -= 1
        # updating length
        res = max(res, curr) # O(1)
    
    return res

def equalSubstring(s: str, t: str, maxCost: int) -> int:
    if maxCost == 0:
        if s == t:
            return len(s)
        return 1
    left = curr = res = 0
    for right in range(len(s)):
        curr += abs(ord(s[right]) - ord(t[right]))
        while curr > maxCost:
            curr -= (abs(ord(s[left]) - ord(t[left])))
            left += 1
        res = max(res, right - left + 1)
    
    return res

print(equalSubstring("abcd", "bcdf", 3))
print(equalSubstring("abcd", "cdef", 3))
print(equalSubstring("abcd", "acde", 0))

# print(f"a ascii: {ord('a')}")
# print(f"b ascii: {ord('b')}")
# print(f"c ascii: {ord('c')}")
# print(f"d ascii: {ord('d')}")
# print(f"e ascii: {ord('e')}")
# print(f"f ascii: {ord('f')}")