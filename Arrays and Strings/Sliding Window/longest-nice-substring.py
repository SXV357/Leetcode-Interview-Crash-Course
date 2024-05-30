# 1763

def longestNiceSubstring(s: str) -> str:
    """
    For every letter of the alphabet that `s` contains it appears both in uppercase and lowercase. Find longest nice substring. COME BACK TO THIS LATER TO TRY SLIDING WINDOW APPROACH  
    """
    # Brute force solution
        # Run time: O(2^n - n)
        # Space complexity: O(2^n - n) because the array stores those many substrings excluding all the individual characters
    if len(s) == 1:
        return ""
    
    substrings = []

    # O(n^2)
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            substrings.append(s[i:j+1])
        
    max_len, curr = 0, ""
    # O(2^n - n): 2^n substrings excluding number of individual characters
    for sub in substrings:
        count = 0
        is_valid = False
        # Variable since a set of substrings will have the same length but will vary across different sets
        for char in sub:
            if char.islower() and char.upper() in sub:
                count += 1
            elif char.isupper() and char.lower() in sub:
                count += 1
        
        # All operations down here are O(1)
        if count == len(sub):
            is_valid = True
        
        if is_valid:
            if len(sub) > max_len:
                max_len = len(sub)
                curr = sub
    
    return curr

print(longestNiceSubstring("YazaAay"))
print(longestNiceSubstring("Bb"))
print(longestNiceSubstring("c"))