# 2225

from typing import List
from collections import defaultdict

def findWinners(matches: List[List[int]]) -> List[List[int]]:
    """
    Time complexity: O(nlogn) because the sorting of the dictionary dominates everything else - in the case
    where every single value in every single match array is unique we have n keys which we need to sort
    Space complexity: O(n) because in the worst case the hashmap stores n keys. similarly with the result array
    one of the subarrays could hold all n elements and none in the other or even n/2 in one and n/2 in the other
    but n dominates
    """
    # count = defaultdict(lambda: [0, 0])
    # for winner, loser in matches:
    #     count[winner][0] += 1
    #     count[loser][1] += 1

    count = defaultdict(int) # dictionary to map players to their number of losses
    for winner, loser in matches:
        # it need not be the case that a certain player just loses games only because they could also win
        # at the same time, we may not account for the winners if we just use the losing players, hence
            # whenever we encounter a winner that hasn't lost yet we set its count to 0 because for all the losers
            # we don't want to reset their count and lose the data
        if not count[winner] > 0:
            count[winner] = 0
        count[loser] += 1 # this needs to be done to update number of losses
        
    count = dict(sorted(count.items())) # since the values in the result need to be returned in ascending order we sort the keys to handle that before
    res = [[], []] # to store the players who have lost 0 games and those who have lost just 1 game
    for k in count.keys():
        # answer[0] is a list of players who haven't lost any games(losses = 0)
        if count[k] == 0:
            res[0].append(k)
        # answer[1] is a list of players who have lost exactly 1 game(losses = 1)
        elif count[k] == 1:
            res[1].append(k)
    
    return res    

print(findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))
print(findWinners([[2,3],[1,3],[5,4],[6,4]]))