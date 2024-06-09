# 1207

from collections import Counter

def uniqueOccurrences(arr: list[int]) -> bool:
    """
    Time complexity: O(n) to populate the hashmap and to convert the frequencies array to a set
    Space complexity: O(n) to store `n` key/value pairs in the hashmap in the worst case
    """
    freq = Counter(arr) # get the frequency of all elements in the array
    # if the number of occurrences is unique then even after converting it to a set its length won't change with respect to the original array and vice-versa which is what we check for
    return len(set(freq.values())) == len(freq.values())

print(uniqueOccurrences([1,2,2,1,1,3]))
print(uniqueOccurrences([1,2]))
print(uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))