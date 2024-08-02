# 649

from collections import deque

def predictPartyVictory(senate: str) -> str:
    """
    Time complexity: O(n)
    - Loop through the string adding indices of the characters to the queues
    - while loop where the simulation happens
    Space complexity: O(n) if we take into account the combined space taken up by both the queues
    """
    # straightforward - no other senators to ban so can declare victory directly
    if len(senate) == 1:
        return "Radiant" if senate == "R" else "Dire"
    # the first senator can always ban the second senator and the first senator can always win
    elif len(senate) == 2 or len(set(senate)) == 1:
        return "Radiant" if senate[0] == "R" else "Dire"

    n = len(senate)
    rq, dq = deque(), deque()
    # loop for adding indices of all the R's and D's to their respective queues
    for i in range(n):
        if senate[i] == "R":
            rq.append(i)
        if senate[i] == "D":
            dq.append(i)
    
    # the relative order in which a senator takes an action matters so we always compare the first two elements in each queue and keep going until there's only 1 kind of senator left standing
    while rq and dq:
        smaller = rq[0] < dq[0]
        if smaller:
            el1 = rq.popleft()
            dq.popleft()
            rq.append(el1 + n)
        else:
            el2 = dq.popleft()
            rq.popleft()
            dq.append(el2 + n)

    if not rq:
        return "Dire"

    return "Radiant"

print(predictPartyVictory("RD"))
print(predictPartyVictory("RDD"))