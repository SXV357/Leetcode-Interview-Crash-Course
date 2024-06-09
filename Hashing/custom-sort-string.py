# 791

from collections import Counter

def customSortString(order: str, s: str) -> str:
    """
    - Build the permutation using string concatenation and string multiplication - Not optimal
    - Build the permutation by appending characters to an array and using string multiplication - Not optimal
    - Build the permutation by appending characters to an array and w/o using string multiplication - Optimal

    Time complexity: Let `len(order) = m` and let `len(s) = n`. Overall complexity: O(x(m + n) + m) for the following:
    - In the worst case every single character in `order` appears in the frequency map of `s` so we iterate `m` times in the outer loop and let's assume that the frequency of this character on average in `s` is `x` hence we iterate `x` times in the inner loop giving a complexity of O(m * x)
    - In the worst case, no characters in `order` appear in the frequency map of `s` so we iterate `n` times over all key/value pairs in `freq` with all frequencies > 1 and once again assuming the average frequency is `x` we iterate `x` times in the inner loop giving a complexity of O(n * x)
    - The string joining at the end takes O(m) time because in the case where every single character of `order` appears in the frequency map of `s` then `m` items are appended to `res`

    Space complexity: O(n + m) because of the following reasons
    - O(n) because freq would store `m` key/value pairs if every single character in `s` is unique
    - O(m) as discussed before where `res` could store `n` values when every single character of `order` appears in `s`
    """
    # Original approach

    # res = ""
    # for char in order:
    #     if char in freq:
    #         res += (freq[char] * char)
    #         freq[char] = 0
    
    # for k, v in freq.items():
    #     if v > 0:
    #         res += (v * k)
    
    # return res

    # More optimal approach

    freq = Counter(s) # this stores the frequency of all the characters in s
    res = [] # this list will store the characters in the order of how the permutation needs to be constructed

    for char in order:
        # since the permutation of s needs to have the characters in the same order as they are in order, we iterate from the start of order and check if each character exists in the hashmap in O(1) time
        if char in freq:
            # we are told that all characters in order are unique but that need not be true for s so for how many ever times this character occurs we add it to the array(follows the rule that the relative order needs to be maintained)
            for _ in range(freq[char]):
                res.append(char)
            freq[char] = 0 # we have exhausted all of this character so we can update the dictionary count to 0. this is necessary because it is not guaranteed that every character in order exists in s so in order to fully build the permutation we need to keep track of this
    
    # at this point we have the characters that will form the permutation only for ones that are common to order and s but we also need to take into account the characters in s that don't exist in order
    for k, v in freq.items():
        # all the common chars are used up so we check if anything else's frequency is greater than 0
        if v > 0:
            # this character only in s could occur more than once so we include the character those many times
            for _ in range(v):
                res.append(k)
    
    return "".join(res) # once we have everything we need for the permutation we join everything together and return it

print(customSortString("cba", "abcd"))
print(customSortString("bcafg", "abcd"))
print(customSortString("kqep", "pekeq"))