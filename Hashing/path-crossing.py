# 1496

from collections import defaultdict

def isPathCrossing(path: str) -> bool:
    """
    Time complexity: O(n^2) since we iterate `n` times through the string in the worst case and each time, we are converting the fixed size array to a tuple which takes O(2) time but due to collisions can be O(n) in the worst case
    Space complexity: If we never encounter a previously visited location we store `n` keys in the hashmap and everything else such as the start array takes up constant space for purposes of the problem
    """

    visited = defaultdict(int) # this will be used to keep track of visited locations along with their frequencies so that can we can detect when we are on a location we have previously visited
    start = [0, 0] # this is the starting position
    visited[tuple(start)] = 1 # this needs to be included in the hashmap since we are starting here and its possible that we might come back here in the future

    for move in path:
        # based on the direction we update the respective position in the location array where start[0] = x and start[1] = y
        if move == "N":
            start[1] += 1
        elif move == "S":
            start[1] -= 1
        elif move == "E":
            start[0] += 1
        elif move == "W":
            start[0] -= 1

        # keys cannot be mutable so convert it to a tuple and when we check if it exists in the dictionary and if so we return true because we are on a location we have previously visited 
        if tuple(start) in visited:
            return True
        # if this is a new location then we simply update its frequency in the hashmap
        visited[tuple(start)] += 1
    
    return False

print(isPathCrossing("SS"))
print(isPathCrossing("NES"))
print(isPathCrossing("NESWW"))