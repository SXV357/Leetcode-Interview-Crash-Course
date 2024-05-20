# 125

def isPalindrome(s: str) -> bool:
    """
    Time complexity: O(n) - the while loop can only iterate a max of n times since the pointers start at the ends of the string and move towards each other
    Space complexity: O(n) - at worst if there are no non-alphanumeric characters in s then all characters in the string are added to the list
    """
    modified_chars = []
    # if the current character is an alphanumeric character add it to the list of matching characters
    for char in s: # O(n)
        if char.isalnum(): # O(1)
            modified_chars.append(char.lower()) # O(1)
    s = "".join(modified_chars) # O(n) - concatenate all the valid characters into a string and reassign it to s
    l, r = 0, len(s) - 1
    # palindrome checking logic: if at any point the characters at both indices are not the same the string is not a palindrom
    while l < r: # O(n)
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))