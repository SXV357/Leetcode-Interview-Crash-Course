# 1657

from collections import Counter

def closeStrings(word1: str, word2: str) -> bool:
    """
    Time complexity: Let `len(word1) = x` and let `len(word2) = y`. Then the complexity is O(xlogx + ylogy) ignoring all constants
    - Converting both strings to a set takes O(x + y) time where O(x) for `word1` and O(y) for `word2`
    - Iterating through `s1` takes O(x) time in the worst case if every single value in `s1` also exists in `s2`
    - Obtaining frequency map from both strings takes O(x + y) time once again
    - Sorting the values array of both hashmaps takes O(xlogx) and O(ylogy) time respectively

    Space complexity: O(x + y) because we are storing 2 sets which can hold `x` and `y` elements at most respectively and also because if every single char is unique in both the strings the frequency maps also store `x` and `y` key/value pairs respectively
    """
    # if the words are already equal then we can return true as no operations need to be done
    if word1 == word2:
        return True
    
    # only swapping and replacing are allowed but deletion is not allowed so if the lengths don't align then its impossible to obtain one string from the other
    if len(word1) != len(word2):
        return False

    # as said before deletion is not allowed so if there are some characters in word1 that don't exist in word2 and vice-versa then we can never make the strings equal each other hence we check whether both strings contain the exact same characters after converting them to a set
    s1, s2 = set(word1), set(word2)
    for val in s1:
        if val not in s2:
            return False
    
    # now that we know both strings have the same set of characters we get the frequency of the characters in each string
    freq_one, freq_two = Counter(word1), Counter(word2)
    # if we want to obtain one string from the other and given what operations can be performed the frequencies of the unique characters must match in both the strings, i.e, if we sort the frequencies then they must be equal
    return sorted(freq_one.values()) == sorted(freq_two.values())

print(closeStrings("abc", "bca")) # true
print(closeStrings("a", "aa")) # false
print(closeStrings("cabbba", "abbccc")) # true
print(closeStrings("abbzzca", "babzzcz")) # false