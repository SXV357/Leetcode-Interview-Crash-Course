# 1436

from collections import defaultdict

def destCity(paths: list[list[str]]) -> str:
    """
    Time complexity: O(n) in the worst case if all the cities are unique although the problem states that it will never be the case because a destination city would always never exist
    Space complexity: O(n) because we would store `2n` keys in the worst case but we ignore the constant
    """

    freq = defaultdict(int) # this dictionary instead of mapping cities to their frequency will keep a track of a running counter of how many times it is a source city vs how many times it is a destination city

    for cityA, cityB in paths:
        freq[cityA] += 1 # this is always the source so we increment the counter for it
        freq[cityB] -= 1 # this is always the destination so we decrement the counter for it
    
    # if a city was only a destination city and never was a source city its count in the dictionary would be negative hence we check for that as we're iterating through all key/value pairs and then return the appropriate key
    
    for k, v in freq.items():
        if v < 0:
            return k
    
    return None

print(destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
print(destCity([["B","C"],["D","B"],["C","A"]]))
print(destCity([["A","Z"]]))