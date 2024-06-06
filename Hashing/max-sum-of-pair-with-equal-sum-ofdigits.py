# 2342

from collections import defaultdict

def digSum(num: int) -> int:
    """
    Time complexity: O(n) - we need to accumulate the sum of all the `n` digits of `num`
    Space complexity: O(1) because we're storing just one variable to keep track of the sum that is independent of input size
    """
    res = 0
    while num > 0:
        res += num % 10
        num //= 10
    return res

def maximumSum(nums: list[int]) -> int:
    """
    Time complexity: O(n * (m + log(n) + 1)) - assuming `len(nums) = n` and the average number of digits in a given value is `m` we are calculating the sum of the digits for all those `n` numbers, then sorting the arrays of `n` keys in the worst case and similarly iterating `n` times in the worst case at the very end
    Space complexity: O(n * m) because if every single value in the array has the same digit sum we have just one key with `n` values in the value array in the worst case
    """
    mappings = defaultdict(list) # this will map the sum of the digits to the values that result in that sum
    res = -1 # this will store the result of the maximum value of the two indices
    for _, val in enumerate(nums):
        mappings[digSum(val)].append(val) # updating the hashmap with the sum of the digits and mapping it to all the values with that digit sum
    
    # the reason we're sorting the arrays is because for a given digit sum we only care about the maximum value of the sum of the values at any two indices which satisfy that constraint
    for k in mappings.keys():
        mappings[k].sort()

    # its pointless considering arrays of size equal to 1 because there's only one value in the array to consider but for everything else the sum between the indices will be maximized when we take the sum of the last two values hence we use that to update res
    for v in mappings.values():
        if len(v) > 1:
            res = max(res, v[-1] + v[-2])
    
    return res

print(maximumSum([18,43,36,13,7]))
print(maximumSum([10,12,19,14]))
print(maximumSum([279,169,463,252,94,455,423,315,288,64,494,337,409,283,283,477,248,8,89,166,188,186,128]))