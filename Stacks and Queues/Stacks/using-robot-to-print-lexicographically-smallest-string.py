# 2434

from collections import Counter
import sys

def get_min_char(frequencies):
    min_char_val = sys.maxsize
    for char, frequency in frequencies.items():
        if frequency != 0:
            min_char_val = min(min_char_val, ord(char))
    
    return chr(min_char_val) if min_char_val != sys.maxsize else 'a'

def robotWithString(s: str) -> str:
    freq = Counter(s)
    res, t = [], []
    for char in s:
        t.append(char)
        freq[char] -= 1
        while t and t[-1] <= get_min_char(freq):
            res.append(t.pop())

    while t:
        res.append(t.pop())
    
    return "".join(res)

print(robotWithString("bydizfve"))
print(robotWithString("zza"))
print(robotWithString("bac"))
print(robotWithString("bdda"))