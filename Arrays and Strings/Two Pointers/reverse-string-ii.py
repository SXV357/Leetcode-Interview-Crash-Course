# 541

def reverse(l: int, r: int, arr: list[str]) -> None:
    """
    Reverses all characters between the indices specified by l and r
    Time complexity: O(r - l + 1) - the pointers are spaced at this distance from one another
    Space complexity: O(1) - no variabls or extra space being used
    """
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

def reverseStr(s: str, k: int) -> str:
    """
    Time complexity: O(k // n)
    Space complexity: O(n) because we are storing all characters of s in an array and it will grow as length of s increases
    """
    # if we have exactly enough characters to reverse or less than what k is the maximum number of characters that can be reversed is the length of the string
    if k >= len(s):
        return s[::-1] # O(n) since assumption is that in the background we loop in the reverse direction and concatenate all chars to another string
        
    chars = list(s) # convert string into array of chars so the swapping/reversal can be done
    for i in range(0, len(chars) - 1, 2 * k): # move in increments of 2k since we're reversing k chars every 2k chars
        # we need at least k characters after the current index to be able to do the reversal
        if i + k <= len(chars):
            reverse(i, i + k - 1, chars) # i + k - 1 accounts for all k characters including current one
        else:
            remaining_chars = len(chars) - i # there's not enough characters to reverse because we are close to the end of the string
            # Case 1: < k chars left so reverse everything remaining(starting from i + k till the end)
            if remaining_chars < k:
                reverse(i, len(chars) - 1, chars)
            # Case 2: < 2k chars but >= k chars - leave everything else as is
            if (remaining_chars < (2 * k)) and (remaining_chars >= k):
                pass
    
    return "".join(chars) # concatenate modified char array into a string and return it

print(reverseStr("hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl", 39))