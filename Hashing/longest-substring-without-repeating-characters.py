# 3

from collections import defaultdict

def lengthOfLongestSubstring(s: str) -> int:
    """
    Time complexity: O(n) - amortized runtime
    Space complexity: O(n) for including the dictionary because we could have `n` keys at the greatest if every character occurs exactly once else O(1)
    """

    freq = defaultdict(int) # this is for storing the frequency of characters in the string and will be built as the string is traversed
    left = res = 0 # left pointer and variable to keep track of the length of the longest substring
    for right in range(len(s)):
        freq[s[right]] += 1 # updating the frequency of this character in the string
        while freq[s[right]] > 1: # since we want a substring where every character occurs only once we cannot have any characters at all that have a frequency > 1 hence this while loop is used to detect that
            # we technically don't need both the checks as we can simply do something like freq[s[left]] -= 1 since we will be updating the count of everything in the substring so far and will eventually also update the count of the element whose frequency has been violated
            if s[left] == s[right]:
                freq[s[right]] -= 1
            else:
                freq[s[left]] -= 1
            left += 1
        res = max(res, right - left + 1) # now that the substring is valid we update its count
    
    return res

print(lengthOfLongestSubstring("tmmzuxt"))
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))