# 2260

import sys

def minimumCardPickup(cards: list[int]) -> int:
    """
    Time complexity: O(n) because we perform a single pass through the array iterating over `n` elements with all operations inside the loop happening in constant time because they involve either a hashmap or an arithmetic operation
    Space complexity: O(n) because in the case where every single value is unique then we store `n` keys
    """

    # Brute force solution - TLE
    
    # res = sys.maxsize
    # for i in range(len(cards)):
    #     curr = 1
    #     j = i + 1
    #     while j < len(cards):
    #         curr += 1
    #         if cards[j] == cards[i]:
    #             res = min(res, curr)
    #             break
    #         j += 1
    
    # return res if res != sys.maxsize else -1

    # Optimal solution using a hashmap(Sliding window can also be used but isn't that optimal)

    res = sys.maxsize # this variable is for keeping track of the minimum number of cards to be picked up
    mappings = {} # this dictionary will map the value in the array to its last seen index
    for i, val in enumerate(cards):
        # we simpy map the integer to the index where it was last seen in the array
        if val not in mappings:
            mappings[val] = i
        else:
            # at this index we have once again seen the number and since we know what index this number was last seen via the hashmap we can calculate the minimum number of cards
            res = min(res, i - mappings[val] + 1)
            # this is so that if there is a smaller numbe of cards that can be picked with the number starting at this index we calculate that as well
            mappings[val] = i
        
    return res if res != sys.maxsize else -1 # if every single value is unique then the result variable never gets updated so we add a check for that and return -1 in that case

print(minimumCardPickup([3,4,2,3,4,7]))
print(minimumCardPickup([1,0,5,3]))