# 49

from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    """
    Time complexity: O(n^2 * logn) because we initially iterate through all strings which happens in O(n) time and then we sort them which happens in O(nlogn) time - we sort every single string in the input array so it multiplies out
    Space complexity: O(n^2) since in the case that every string in `strs` has a unique sorted string then the dictionary stores `n` unique keys and along with each key there is an array consisting of just a single value which is that unique string
    """
    # PREV SOLUTION: TLE
    
    # groups = set()
    # for string in strs:
    #     groups.add("".join(sorted(string)))
        
    # res = []
    # for val in groups:
    #     curr = []
    #     for string in strs:
    #         if "".join(sorted(string)) == val:
    #             curr.append(string)
    #     res.append(curr)
    
    # return res

    groups = defaultdict(lambda: []) # this is the dictionary that maps the sorted string to a list of the original strings

    # the logic below is for updating the hashmap
    for string in strs:
        groups["".join(sorted(string))].append(string)
    
    # since we just want the groupings we could simply return groups.values() but the logic below iterates through all the keys of the dictionary and appends the respective groups to the result and then returns it
    res = []
    for k in groups.keys():
        res.append(groups[k])
    
    return res

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams(["ddddddddddg","dgggggggggg"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))