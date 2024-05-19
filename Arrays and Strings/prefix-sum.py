# Main idea behind prefix sum:
    # prefix array for some arbitrary array maintains a running sum up till a specific index
        # for example last element in the prefix array contains sum of all elements in original array until that specific index
    # prefix array calculated first and then used in subsequent parts of the algorithm which can be done in O(1) time
    # formula for sum of a subarray from index i to index j: prefix[j] - prefix[i] + original array[i]

def determine_query(nums: list[int], queries: list[list[int]], limit: int) -> list[bool]:
    """
    Time complexity: O(n + m) - Build prefix array in O(n) time and build result array in O(m) time since its dependent on size of queries array
    Space complexity: O(n + m) - for prefix array and for the result array since both scale linearly with input size
    """
    prefix = [nums[0]]
    # Logic to build the prefix array
    # We start with adding the very first element in nums since the running sum of the first 1 elements is just the first element
    # From there on out, we simply add the sum of the last element in the prefix array to the current element in the original array
        # The last element in the prefix array always stores the sum of the array uptil that specific index, so
            # if we add that to the current element, we get the next index in the prefix array as being the sum until the next index
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    
    print(f"Prefix array: {prefix}")

    # Another approach to calculating sum between 2 indices:
        # prefix[end index] - prefix[start index - 1] (this only works if start index != 0)
            # get sum of all elements until end index and subtract sum of all elements until one before the start index
            # this will isolate the subarray and give the sum we're looking for
        # otherwise use the other approach
    
    res = []
    for j in range(len(queries)):
        x, y = queries[j][0], queries[j][1]
        # To get the sum of a subarray specified by indices i and j, the following formula is used:
            # prefix[end index] - prefix[start index] + original[start index]
        # The reason why this approach works is the following:
            # prefix[end index] gives the sum of everything until the end index
            # prefix[start index] gives sum of everything until the start index
            # when we subtract the two from each other, we have isolated the subarray we are interested in
            # now, if we add the element in the original array associated with start index we get the sum between the two indices
        if prefix[y] - prefix[x] + nums[x] < limit:
            res.append(True)
        else:
            res.append(False)

    return res 

def waysToSplitArray(nums: list[int]) -> int:
    """
    Time complexity: O(n) - building the prefix array and also moving through the array for determining number of valid splits
    Space complexity: O(n) because of prefix array as it scales linearly with growth of input array
    """
    prefix = [nums[0]]
    # Building the prefix array as usual
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    
    print(f"Prefix array: {prefix}")
        
    num_valid, n = 0, len(nums)
    for j in range(n - 1): # we only iterate until n - 1 because a split at the very last index is not possible
        # the sum of the first half is simply the corresponding index in the prefix array since it contains the sum of all elements until that index
        # sum of the remaining elements apart from the representation below can also be represented as
            # prefix[-1] - prefix[j] (take the sum of all elements in the array and subtract the sum of everything until the current index which will give sum of the remaining elements)
            # we can use this because we never deal with the 0 index and can thus avoid out of bounds errors 
        first, remaining = prefix[j], prefix[n - 1] - prefix[j + 1] + nums[j + 1]
        # 2nd check is technically not necessary since we're looping over the first n - 1 elements so it is guaranteed that there will be atleast one element after the element at the current index
        if (first >= remaining) and (0 <= j < n - 1):
            num_valid += 1
    
    return num_valid

def runningSum(nums: list[int]) -> list[int]:
    """
    Time complexity: O(n) - One pass through all the elements of the array
    Space complexity: O(n) since we're using a prefix array that grows with input size
    """
    # builds a running sum of the array by calculating the prefix array for each index(sum of all elements until that specific index)
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    
    return prefix

def minStartValue(nums: list[int]) -> int:
    """
    Time complexity: O(x * n) where x = (n/2) * (m-1) + 1 so O(n^2 * m)
    Space complexity: O(n) - O(n) for the prefix array and O(1) for everything else but O(n) dominates so we only care about that
    ** Come back to this problem later on and read through editorial solution for optimal prefix sum approach **
    """
    # if all items in nums are >= 1 and we start with 1 as our startValue we always only achieve a sum >= 1 so the min possible value is 1
    if all(i >= 1 for i in nums): # O(n) because all elements need to be checked
        return 1
    
    prefix = [nums[0]]
    # building prefix array
    for i in range(1, len(nums)): # O(n)
        prefix.append(nums[i] + prefix[-1])

    # we need to find an approximation for x(# of times the outer loop runs) to calculate actual time complexity
    # let n = number of elements in nums, m = absolute value of most negative number in nums
    # we are finding worst case time complexity so let's assume an array where n/2 elements are (1) and the remaining elements are (-m)
        # let's take the example: [1, 1, 1, -4, -4, -4] with n = 6 and m = 4
    # the key here is to realize that we need such a start value which when added to all positive elements and negative elements will never yield a sum < 1
    # the total sum of the first n/2 elements is simply n/2 since they're all 1's and the total sum of all negative elements is (n/2) * m
        # here n/2 is 3 which is the sum of the first 3 elements precisely and sum of all negative elements is -12 which is 3 * 4 which is the same as (n/2) * m
    # now, one thing to also note is that if we select too small of a start value then the sum of all the negative elements will overpower it and thus
        # the idea is that the sum of the initial value and the first n/2 elements must be atleast as great as the sum of the remaining elements to ensure the sum never drops below 1
        # thus, start val + (n/2) >= (n/2) * m
        # solving for start value gives: start val >= (n/2) * (m - 1)
        # we now add a 1 to the end because we want to ensure the overall sum is always > 1
            # it can equal 1 as well since that is valid but we want to avoid it in case there are some values which may cause unnecessary fluctuations

    # the loop down below calculates the min possible start value by repeatedly comparing intermediate sums of the current start value with every value in the array
    start, flag = 1, False
    while True: # runs an arbitrary number of times lets say x
        j = 0
        # in this loop using the prefix array we check if there are any instances of the cumulative sum dropping below 1 involving the current start value
        while j < len(prefix): # O(n)
            if start + prefix[j] < 1:
                flag = True
                break
            j += 1
        
        # this start value produces an instance of the sum being less than 1 so we check the next element
        if flag:
            start += 1
            flag = False
        else: # no issues with this start value and we can return it right away
            break
    
    return start

def getAverages(nums: list[int], k: int) -> list[int]:
    """
    Time complexity: O(n) to build the prefix array and O(n - k) for the loop at the end so O(n) since (n >= n - k)
    Space complexity: O(n) - prefix array grows with input size and result array grows with input size
    """
    # base cases
        # k is larger than the length of the list
        # k is 0
    # if k is greater then the length of the input list then are aren't enough elements to consider on the left and right of a particular index to calculate the average
    if k > len(nums):
        return [-1] * len(nums)
    # if k = 0 then there's no need to consider any elements at all to the left and right of a given index and we can just return the array as is right away
    if k == 0:
        return nums

    # building the prefix array since it will be useful for computing the sum of values between two indices when actually updating result list
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])

    # elements at all indices < k will have a value of -1 since there aren't k elements to the left of them that can be considered for the sum
    res = [-1] * len(nums)
    # we start iterating from the element at the kth index since it could very well be the case that it has k elements both to its left and right 
    for j in range(k, len(nums)):
        # we already know that starting the kth index there will always be >= k elements to the left but we also need to check whether we have >= k elements on the right
        # if that's true we can calculate the subarray average
        if ((len(nums) - 1) - j) >= k:
            # using the formula for calculating the subarray average(j + k is the right pivot index and j - k is the left pivot index)
            curr_sum = prefix[j + k] - prefix[j - k] + nums[j - k]
            # divide by 2k + 1 since we are account for 2k elements to the left and right including the element at the current index itself
            res[j] = (curr_sum // ((2 * k) + 1))
        # there are >= k elements on the left but not enough on the right so we cannot calculate the subarray average and hence set the value to be -1
        else:
            res[j] = -1
    
    return res

def largestAltitude(gain: list[int]) -> int:
    """
    Time complexity: O(n) - O(n - 1) times for the loop and O(n + 1) to find the maximum value in the prefix array but ignoring constants its O(n)
    Space complexity: O(n) - prefix array contains running sum of gain array including a 1 at the beginning so technically O(n + 1) but ignoring constants its O(n)
    """
    prefix = [0, gain[0]] # start trip with altitude equal to 0
    # building prefix array to calculate altitudes at a given point since we're given the net gain in altitude in the original array
    for i in range(1, len(gain)):
        prefix.append(gain[i] + prefix[-1])
    return max(prefix) # end up with array of altitudes at the end and we want to find the highest altitude of a given point

def pivotIndex(nums: list[int]) -> int:
    """
    Time complexity: O(n) - to build the prefix array and to iterate over all numbers and calculate the pivor indices
    Space complexity: O(n) - prefix array only since it is linearly dependent on the input list
    """
    # building the prefix array
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    
    for j in range(len(nums)):
        # sum of all elements strictly to the left of the current index. if we're at the first element, no elements to the left so sum is 0
        left = 0 if j == 0 else prefix[j - 1]
        # sum of all elements strictly to the right of the current index. if we're at the last element, no elements to the right so sum is 0
            # unlike modifying which index of pivot array we're dealing with for the left sum the following formula below to calculate sum of all elements
            # on the right adjusts itself because we get sum of all elements of the array - sum of all elements until the current index leaving sum of all elements strictly to the right of it
        right = 0 if j == len(nums) - 1 else prefix[-1] - prefix[j]
        if left == right:
            return j
        
    return -1

class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        Builds a prefix array using the list nums and returns the sum of the elements between indices left and right inclusive
        """
        prefix = [self.nums[0]]
        for i in range(1, len(self.nums)):
            prefix.append(self.nums[i] + prefix[-1])
        
        return prefix[right] - prefix[left] + self.nums[left]