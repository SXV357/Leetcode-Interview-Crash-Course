# 451

from collections import Counter

def frequencySort(s: str) -> str:
    """
    Time complexity: O(n(logn + x))
    - Build the frequency map for which we need to iterate over all `n` characters: O(n)
    - Sort all the `n` key/value pairs in the dictionary: O(nlogn)
    - Iterate over the sorted dictionary which takes O(n) time and assuming that each character occurs `x` times on average we iterate `x` times in the inner loop giving a loop compelxity of O(nx)

    Space complexity: O(n) because in the worst case the hashmap stores `n` key/value pairs and the array would also end up storing those many values
    """
    freq = Counter(s) # store the frequency of all elements in the string
    modified = [] # will store the characters that form the newly sorted string
    # since we want to sort the string in decreasing order by character frequency we iterate over the sorted dictionary by value in descending order
    for k, v in sorted(freq.items(), key = lambda x: x[1], reverse=True):
        # compared to appending char * char count to a string which is quite expensive we iterate over how many of this character exist and add those many to the array
        for _ in range(v):
            modified.append(k)
    
    return "".join(modified) # at the end we join everything together and return it

print(frequencySort("tree"))
print(frequencySort("cccaaa"))
print(frequencySort("Aabb"))