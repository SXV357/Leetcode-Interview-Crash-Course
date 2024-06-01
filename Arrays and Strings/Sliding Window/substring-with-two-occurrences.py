# 3090

# from collections import Counter

def maximumLengthSubstring(s: str) -> int:
    # Brute force solution(899 ms runtime)

    max_len = 0

    # for i in range(len(s)):
    #     for j in range(i + 1, len(s)):
    #         occurrences = dict(Counter(s[i:j+1]))
    #         flag = True
    #         for val in occurrences.values():
    #             if val > 2:
    #                 flag = False
    #                 break
            
    #         if flag:
    #             max_len = max(max_len, j - i + 1)
    
    # Sliding window solution(42 ms runtime)

    # We keep expanding the window as long as the count of all characters inside is <= 2
    # If this condition is broken, we keep shrinking the window until the count of everything inside is <= 2
    # After we update the length of the longest window

    l, occurrences, seen = 0, {}, set()
    for r in range(len(s)):
        if s[r] not in seen:
            seen.add(s[r])
            occurrences[s[r]] = 1
        else:
            occurrences[s[r]] += 1
        
        while occurrences[s[r]] > 2:
            if s[l] == s[r]:
                occurrences[s[r]] -= 1
            else:
                occurrences[s[l]] -= 1
            l += 1
        
        max_len = max(max_len, r - l + 1)

    
    return max_len

print(maximumLengthSubstring("bcbbbcba"))
print(maximumLengthSubstring("aaaa"))
print(maximumLengthSubstring("dcfdddccb"))