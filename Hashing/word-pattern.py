# 290

from collections import defaultdict

def wordPattern(pattern: str, s: str) -> bool:
    """
    Time complexity: Let `len(pattern) = x` and `len(words) = y`. O(y) is the overall complexity because of the following reasons:
    - Iterating over every single word in `words` takes O(y) time since all the operations inside the first loop take place in O(1) time
    - The second loop also takes place in O(y) time since in the worst case we have `y` key/value pairs in the dictionary because of every word being unique and as usual the inner operations take place in O(1) time
    - The third loop happens in O(y) time as well because of the same reasoning as above and because of the fact that the operations inside it happen in O(1) time. One thing to note is that the set->list conversion happens in O(1) time because as of this point we know the length of all sets is 1 so we can ignore it

    Space complexity: O(y) because of the following reasons
    - Storing `words` in memory takes up O(y) space
    - The hashmap can store `y` key/value pairs in the worst case if every single word is unique
    - The set can also store `y` values in the worst case for the same reasoning above
    """
    words = s.split(" ") # do this to get all the words in s
    # this is a straightforward case because if the lengths are not equal the condition of a bijection existing between a letter in pattern and a non-empty word in s is violated
    if len(pattern) != len(words):
        return False
    
    mappings = defaultdict(set) # this dictionary will map words in s to the corresponding letters in pattern but we use a set so that we can for uniqueness of mappings
    for i in range(len(words)):
        mappings[words[i]].add(pattern[i])
    
    # Case 1: There is some word in s that is associated with more than one letter in pattern violating the uniqueness condition so we return false
    for v in mappings.values():
        if len(v) > 1:
            return False
    
    # Case 2: Each word in s maps to some character in pattern but there are two different words that could map to the same letter and we check for that here
    seen = set()
    for x in mappings.values():
        curr = list(x)
        # if this letter in pattern is already associated with some word then that means the bijection condition is violated and we can return false right away
        if curr[0] in seen:
            return False
        seen.add(curr[0])
    
    return True

print(wordPattern("abba", "dog cat cat dog"))
print(wordPattern("abba", "dog cat cat fish"))
print(wordPattern("aaaa", "dog cat cat dog"))
print(wordPattern("aaa", "aa aa aa aa"))