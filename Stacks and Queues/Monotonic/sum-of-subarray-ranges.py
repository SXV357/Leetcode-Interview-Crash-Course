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

print(subArrayRanges([1,2,3]))
print(subArrayRanges([1,3,3]))
print(subArrayRanges([4,-2,-3,4,1]))