# 1189

from collections import Counter

def maxNumberOfBalloons(text: str) -> int:
    curr = 0
    orig, freq = Counter("balloon"), Counter(text)
    for k in freq.keys():
        if k in orig and freq[k] >= orig[k]:
            curr += 1
    
    res = 0
    if curr == 5:
        while freq["b"] > 1 and freq["a"] > 1 and freq["l"] > 2 and freq["o"] > 2 and freq["n"] > 1:
            freq["b"] -= orig["b"]
            freq["a"] -= orig["a"]
            freq["l"] -= orig["l"]
            freq["o"] -= orig["o"]
            freq["n"] -= orig["n"]
            res += 1
        
        return res
    
    return 0

print(maxNumberOfBalloons("nlaebolko"))
print(maxNumberOfBalloons("loonbalxballpoon"))
print(maxNumberOfBalloons("leetcode"))