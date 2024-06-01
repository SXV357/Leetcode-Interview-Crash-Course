# 2932

import unittest

def maximumStrongPairXor(nums: list[int]) -> int:
    """
    XOR: evaluates to 1 only if exactly one of the bits is 1 and the other is 0
    COME BACK TO THIS LATER TO TRY SLIDING WINDOW APPROACH
    """
    res = 0

    # Brute force solution: O(n^2)
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                res = max(res, nums[i] ^ nums[j])
    
    return res


class TestStrongPairXOR(unittest.TestCase):
    def test_one(self):
        self.assertEqual(maximumStrongPairXor([1, 2, 3, 4, 5]), 7)

    def test_two(self):
        self.assertEqual(maximumStrongPairXor([10, 100]), 0)

    def test_three(self):
        self.assertEqual(maximumStrongPairXor([5, 6, 25, 30]), 7)
    
    def test_single_element(self):
        self.assertEqual(maximumStrongPairXor([1]), 0) # length of array is 1

# if __name__ == "__main__":
#     unittest.main()