# 771

from collections import Counter

def numJewelsInStones(jewels: str, stones: str) -> int:
    # freq will store the frequencies of all characters in stones and res will keep track of how many stones are jewels
    freq, res = Counter(stones), 0 

    # Previous approach: 38ms(beats 38.29%)
    
    # for stone in jewels:
    #     if stone in freq:
    #         res += freq[stone]

    # New approach: 32ms(beats 76.31%)

    jewels = set(jewels) # all the characters in jewels are unique but converting it to a set for faster lookup and access

    for stone in freq.keys():
        # every single time a character occurs in stones that also appears in jewels we need to count it. technically we can also iterate through all the characters of stones and for each character that appears in the jewels set we increment the counter so we never have to even use the dictionary(may save more time?)
        if stone in jewels:
            res += freq[stone]
    
    return res

print(numJewelsInStones("aA", "aAAbbbb"))
print(numJewelsInStones("z", "ZZ"))