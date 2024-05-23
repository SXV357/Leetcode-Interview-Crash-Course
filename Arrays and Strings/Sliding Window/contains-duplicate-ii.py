# 219

# Trivial approach:
        # For the current value in the array
            # iterate over remaining n - 1 elements and check for the two conditions
            # if both conditions are satisfied then we return true
        # return false here since we couldn't find a satisfying pair

    # Time complexity: O(n^2), Space complexity: O(1)
    # for i in range(len(nums)):
    #     flag = False
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] == nums[j] and abs(i - j) <= k:
    #             flag = True
    #             break
        
    #     if flag:
    #         return True
    
    # return False

def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    """
    Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array 
    such that nums[i] == nums[j] and abs(i - j) <= k.

    What the problem is essentially asking is that does a window of size k + 1 exist such that it contains duplicate elements?
    Take the array [1, 2, 3, 1] for example with k = 3. The two distinct indices here are 0 and 3 and abs(0 - 3) <= 3 but the size of the window here is 4(k + 1)
    In the window of 4 elements which is [1, 2, 3, 1] the duplicate elements are 1 and they satisfy the condition above hence true

    Example 2: [1, 0, 1, 1] k = 1
    Here we need to find a valid window of size 2 such that it contains duplicate elements
    We have three windows here of size k + 1 which are [1, 0], [0, 1] and [1, 1] and [1, 1] satisfies the condition above since it is a window of size k + 1 and has duplicate elements

    The brute force approach would be iterating through all windows of size k and checking for presence of duplicate elements(TLE)

    if k == 0: # the absolute difference between any pair of indices will always be > k so its not possible
        return False
    
    initial = nums[:k + 1]
    if len(set(initial)) < len(initial): # we have duplicates
        return True
    
    for i in range(1, len(nums)):
        curr = nums[i:i + k + 1]
        if len(curr) < k + 1:
            continue
        if len(set(curr)) < len(curr):
            return True

    return False
    """

    # COME BACK TO THIS QUESTION TO RE-ATTEMPT

    # Optimal solution

    # The key is that instead of iterating through all windows of size k and checking for duplicate elements we will use a sliding window approach with a set

    window = set() # this is used to keep track of duplicate elements because we want to check for the presence of duplicate elements
    l = 0 # left pointer which we will use to keep track of current window size and shrink if the condition is violated

    for r in range(len(nums)):
        # we always want to maintain a window size of k + 1 or as given in the handout: r - l <= k
        # here the constraint is violated but instead of a while loop we just have a single if statement deleting the current left element from the set and moving the pointer until we have a valid window
        if r - l > k:
            window.remove(nums[l])
            l += 1
        # the idea behind this is that at any given time we will only have a max of k + 1 elements in the set and when we check if the current value
            # exists, we are checking whether it is possible to have duplicates within that window and if so we're done with the problem
        if nums[r] in window:
            return True
        # as we encounter a new character each time we add it to the set so that we can keep track of duplicate elements
        window.add(nums[r])

print(containsNearbyDuplicate([1, 2, 3, 1], 3))
print(containsNearbyDuplicate([1, 0, 1, 1], 1))
print(containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))