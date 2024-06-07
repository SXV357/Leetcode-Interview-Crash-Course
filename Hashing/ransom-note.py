# 383

from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
    """
    Time complexity: O(n + m) because assuming that `len(ransomNote) = n` and `len(magazine) = m` then using Counter() requires iterating through those `n + m` characters to get the counts
    Space complexity: O(n + m) because in the case where every single character in `ransomNote` is unique and every single letter in `magazine` is unique the hashmaps together store a combined `n + m` keys
    """
    rc, mc = Counter(ransomNote), Counter(magazine) # getting the frequency of all characters in both the strings
    for ch in ransomNote: # we could technically iterate through the keys of the frequency map for ransomNote only since that would save even more time instead of iterating through every single character
        # simple case: we cannot construct ransomNote if even one of the characters is not present in magazine so we return false right away
        if ch not in mc:
            return False
        
        # we have found this character in the frequency map for magazine but in order to construct ransom where each char in magazine can only be used once we need to have atleast as many characters in the map for magazine and if that's not the case we can return false right away
        if not mc[ch] >= rc[ch]:
            return False

    return True

print(canConstruct("a", "b"))
print(canConstruct("aa", "ab"))
print(canConstruct("aa", "aab"))