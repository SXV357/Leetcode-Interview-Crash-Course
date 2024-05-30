# 1876

def countGoodSubstrings(s: str) -> int:
    """
    Time complexity: O(n - 2) == O(n) because all the operations inside the loop happen in constant time whereas the outer loop iterates through all set of characters
    Space complexity: O(1) - Just one variable to keep track of number of good substrings
    """
    # We are only considering substrings of length 3 so if the input has a length < 3, doesn't make sense to even consider anything at all so we return 0
    if len(s) < 3: # O(1)
        return 0
    
    res = 0
    # running a loop and checking all substrings of length 3 for the conditions
    for i in range(len(s) - 2): # O(n - 2)
        curr = s[i:i + 3] # O(k) == O(3) == O(1)
        # converting to set usually takes O(n) time for a list of size n but here the list is of size 3 so O(3) == O(1)
        if len(curr) == 3 and len(set(curr)) == len(curr):
            res += 1 # O(1)
    
    return res

    

print(countGoodSubstrings("xyzzaz"))
print(countGoodSubstrings("aababcabc"))