# 2104

def alternate_brute_force(nums: list[int]) -> int:
    """
    Time complexity: O(2n^3)
    Space complexity: O(n)
    """

    res = 0
    for i in range(len(nums)): # O(n)
        for j in range(i + 1, len(nums)): # O(n)
            curr = nums[i:j+1]
            res += (max(curr) - min(curr)) # O(2n)
    
    return res

def subArrayRanges(nums: list[int]) -> int:
    """
    Time complexity: O(n^2)
    Space complexity: O(1)
    """

    # this solution essentially re-computes the maximum and minimum along every step of the inner loop using the current value so that we never have to loop through the current subarray to find its max and min

    res = 0
    for i in range(len(nums)):
        curr_max = curr_min = nums[i] # the starting max and min value is the leftmost value and as we extend the subarray past this index, we re-compute what the new maximum and minimum is and then add that to our answer
        for j in range(i + 1, len(nums)):
            curr_max = max(curr_max, nums[j])
            curr_min = min(curr_min, nums[j])
            res += (curr_max - curr_min)

    return res

def sumSubarrayMins(arr: list[int]) -> int:
    # for each number, how many times is this number the minimum of a subarray
        # need to calculate number of subarrays which has this element as a minimum
    
    # monotonically increasing stack
    res, n = 0, len(arr)
    stack = []
    for i in range(len(arr)):
        while stack and arr[i] < arr[stack[-1]]:
            popped_idx = stack.pop()
            left = popped_idx - stack[-1] if stack else popped_idx + 1
            right = i - popped_idx
            res += (arr[popped_idx] * (left * right))
        stack.append(i)
    
    for i in range(len(stack)):
        left = stack[i] - stack[i - 1] if i > 0 else stack[i] + 1
        right = n - stack[i] # the stack is alr in increasing order so to get how many subarrays to the right this elem is a minimum of, just use a reference to the end of the array
        res += (arr[stack[i]] * (left * right))
    
    return res % (pow(10, 9) + 7)

def sumSubarrayMaximums(arr: list[int]) -> int:
    # approach similar to finding sum minimums of all subarrays but use monotonically decreasing stack
    res = 0
    stack = []
    n = len(arr)
    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            popped_idx = stack.pop()
            left = popped_idx - stack[-1] if stack else popped_idx + 1
            right = i - popped_idx
            res += (arr[popped_idx] * left * right)
        stack.append(i)
    
    for j in range(len(stack)):
        l = stack[j] - stack[j - 1] if j > 0 else stack[j] + 1
        r = n - stack[j]
        res += (arr[stack[j]] * l * r)
    
    return res

def optimal(nums: list[int]) -> int:
    # optimal O(n) solution
        # find sum of maximum of all subarrays - logic would be the same as the one down below
        # find sum of minimum of all subarrays - sum of subarray minimums(leetcode problem #907)
        # subtract the two
    
    return sumSubarrayMaximums(nums) - sumSubarrayMins(nums)

print(subArrayRanges([1,2,3]))
print(subArrayRanges([1,3,3]))
print(subArrayRanges([4,-2,-3,4,1]))