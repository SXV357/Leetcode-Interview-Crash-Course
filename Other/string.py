from collections import Counter, defaultdict

s = "adacaccaadadab"

substrings = []
for i in range(len(s)):
    for j in range(len(s)):
        substrings.append(s[i:j+1])

freq = dict(Counter(list(filter(lambda el: el != "", substrings))))
freq = list(filter(lambda el: el[1] > 1, sorted(freq.items(), key = lambda x: x[1], reverse=True)))
freq = list(sorted(freq, key = lambda x: len(x[0]), reverse=True))
# print(freq)

T = "She sells seashells by the seashore"
P = "shore"

def lastOccur(s):
    L = defaultdict(int)
    for i in range(97, 123):
        curr = chr(i)
        L[curr] = s.rfind(curr)
    
    L[""] = s.rfind("")
    return L

def spm(T: str, P: str, L: defaultdict):
    n = len(T)
    m = len(P)

    i = m - 1
    j = m - 1

    while (i <= n - 1):
        if T[i] == P[j]:
            if j == 0:
                return i
            else:
                i -= 1
                j -= 1
        else:
            l = L[T[i]]
            i = i + m - min(j, 1 + l)
            j = m - 1
        
    
    return -1

print(spm(T, P, lastOccur(P)))