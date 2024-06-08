# 205

from collections import defaultdict

def isIsomorphic(s: str, t: str) -> bool:
    # The idea behind isomorphic strings is the follows:
        # 1. the corresponding letter in t can only be used to replace this current letter in s
        # 2. One given character in s cannot be associated with two unique characters in t and vice versa
    
    # the dictionary is essentially going to store the mappings from all unique characters in t to the corresponding letters in s in a set. a set is used here because it will eventually help us detect conditions where theres a 1:2 or 2:1 correspondence
    mappings = defaultdict(set)
    for i in range(len(t)):
        mappings[t[i]].add(s[i])
    
    # Case 1: If a given character in t is associated with two different characters in s then that's invalid so we check for that and return false right away. it is more convenient because we are working directly with a set. if this given character in t was always mapping to the same character in s which is allowed then the set will only have one value which is fine
    for v in mappings.values():
        if len(v) > 1:
            return False
    
    # Case 2: If a given character in s is associated with two difference characters in t so we check for that as well and return false right away. in this case in the hashmap for exactly two keys the same value in the set will be stored so what we do is convert the set into an array and check whether the current value has already been seen and if so we know this value is part of a duplicate mapping and can exit out else we add it to the set and move on until we encounter such an error
    seen = set()
    for x in mappings.values():
        modified = list(x)
        if modified[0] in seen:
            return False
        seen.add(modified[0])
    
    return True # if all mappings are unique and valid we come here and return true

print(isIsomorphic("egg", "add")) # true
print(isIsomorphic("foo", "bar")) # false (both a and r map to o)
print(isIsomorphic("paper", "title")) # true
print(isIsomorphic("badc", "baba")) # false (both b and d map to b while a and c map to a)