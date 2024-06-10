# 567

from collections import Counter, defaultdict

def checkInclusion(s1: str, s2: str) -> bool:
    """
    2 strings are permutations of each other if TFAE:
    - they contain the exact set of characters
    - they contain the same frequency of characters
    - more simpler: they're equal once they have been sorted

    Naive approach(Inefficient as the number of permutations grows extremely large for large input sizes):
    - Generate all the permutations of `s1`
    - For each permutation check whether this permutation is a substring of `s2` i.e. `permutation in s2` and return True if so otherwise false
        - Time complexity: O((n!/n1! * n2! * ... * nk!) * (n + m))
        - The first formula is how many permutations exist for a given `s1` that can contain duplicates where we divide the factorial of `len(s1)` by the product of the factorials of the frequency of all characters in `s1`
        - In the second part its O(n + m) because for each of the unique permuted strings, we check whether its a substring of `s2` and the length of all permutations equals `len(s1)` and let's say `len(s2) = m` hence that way

    More optimal approach but still somewhat brute-forcing it:
    - Iterate in chunks of size `len(s1)` sorting/generating the frequency map for the substring in each chunk and checking whether they're equal either to the sorted version of `s1` or `s1's` frequency map
        - Time complexity: O((m - n + 1) * 3n)
        - Iterate `m - n + 1` times over `s2`
        - For each iteration slice out a string of size `n` which takes O(n) time
        - obtaining frequency maps for both strings and comparing them which takes O(2n) time since we're converting strings of size `n` to the hashmaps

    Optimal solution
    - Time complexity: O(n) amortized
    - Space complexity: O(n + m) because in the worst case where every single character in both strings are unique the frequency maps store a combined `n + m` key/value pairs
    """
    
    # more optimal: iterate in chunks of size len(s1) sorting the strings/generating the frequency maps and comparing if they're equal(better than generating all the permutations of s1 and then performing the checks)
    
    # n = len(s1)
    # for i in range(len(s2) - n + 1):
    #     curr = s2[i:i+n]
    #     if Counter(s1) == Counter(curr):
    #         return True

    # return False

    # sliding window approach(the while loop is actually not needed since an if statement will also work

    freq, n = Counter(), len(s1) # freq will keep track of the frequency of characters in subarrays corresponding to size n
    left = curr = 0 # left pointer and variable to keep track of number of seen elements so far
    s1_map = Counter(s1) # store this because we will be using this for comparison purposes later
    for right in range(len(s2)):
        freq[s2[right]] += 1 # updating the frequency of this element in the hashmap
        curr += 1 # updating number of elements seen
        while curr > n: # if we are looking for a permutation of s1 in s2 then we are looking for substrings of size n so the moment we have seen more than n characters we need to shrink the window until we have a valid one again
            freq[s2[left]] -= 1 # decrement frequency of leftmost element since we're deleting it from thw window
            curr -= 1 # update it again to match the length of s1
            left += 1 # move left pointer to shrink the window
        if s1_map == freq: # the reason we do this is to check whether the same set of characters with the same respective frequencies exist in both hashmaps and if so we can return true right away
            return True
    
    return False

print(checkInclusion("ab", "eidbaooo"))
print(checkInclusion("ab", "eidboaoo"))

# s1, s2 = "abcc", "cab"
# print(set(s1) == set(s2) and sorted(Counter(s1).values()) == sorted(Counter(s2).values()))
# print(Counter(s1) == Counter(s2))