# 680

# PREVIOUS BRUTE FORCE SOLUTION - TLE

def is_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

def validPalindrome(s: str) -> bool:
    # if s is already a palindrome return true
        # if s has length 2 then we can remove any one character and be left with one character which is always a palindrome
    if is_palindrome(s) or len(s) == 2:
        return True
    
    # One thing to note is that if all characters in the string are unique there's no way it can be a palindrome
        # because even if we delete a given character the remaining will all be unique and they cannot form a palindrome
    if len(set(s)) == len(s):
        return False

    # check if we can remove at most one character such that it is a palindrome
    # brute force approach - O(n^3)
    for i in range(len(s)): # O(n)
        remaining = "".join(s[j] for j in range(len(s)) if j != i) # O(n)
        if is_palindrome(remaining): # O(n)
            return True
    return False

# MORE OPTIMAL SOLUTION USING 2-POINTERS
def checkValidPalindrom(s: str) -> bool:
    """
    Visit this problem again tomorrow and attempt it once again without looking at the solution
    Time complexity: O(n) - the while loop runs n times in the worst case since the pointers start at a distance of n from each other and keep moving in until they cross one another
    Space complexity: O(n) - in cases where the chars at the pointer indices aren't equal, we slice the array into two sections which could at the worst could consist of n - 1 elements
    """
    # the idea behind checking whether a string is a palindrome is relatively straightforward but in cases where the string given is not a palindromw.
        # we have the choice of deleting at most one character after which we need to check if the string can be a palindrome
    # a two pointer technique is favorable for this one because we can cut down the time complexity significantly if we do so
    # in the standard brute force approach for the case where the string given is already not a palindrome
        # we loop thru the string deleting the current character and checking whether the remaining characters form a palindromic string for all characters
    
    # start two pointers one at the start index and one at the last index of the array
    l, r = 0, len(s) - 1
    while l < r:
        # if the characters at the corresponding pointers are equal we don't need to consider them anymore and can move both the pointers inwards
        # however if the characters aren't equal, we have two options
            # we could delete the left character and check whether the remaining characters form a palindrome
            # we could delete the right character and check whether the remaining characters form a palindrome
        # there's no guarantee where deleting the left char or right char and checking the remaining chars will give a palindrome so both cases must be checked
        if s[l] != s[r]:
            # the slices below don't involve every single character but only ones within the bound specified by the left and right pointers
                # the reasoning is that if we encountered a left and right character earlier that were equal, deleting either of them may cause the string to not be palindromic in the future
                # hence we don't delete those matching characters and only consider a subproblem in the next character
            remove_left, remove_right = s[l + 1:], s[l:r]
            # if removing either the left char or the right char causes remaining chars to be a palindrome we can return true right away
            return remove_left == remove_left[::-1] or remove_right == remove_right[::-1]
        l += 1
        r -= 1
    
    # example run with s = "abca"
        # a = a and there's no need to delete either of the two since it may cause the string to not be palindromic anymore
        # we move both pointers inside and see that b != c. now if we delete b, we see that "aca" is clearly a palindrome
        # if we delete c we see that "aba" is clearly a palindrome
        # after we have moved past both the "a\'s" on the outer edges, we know that if we delete either b or c we are left with only the other character in the current substring
            # and a single character is always a palindrome
        # another approach instead of considering only the current substring is to include everything and do a check
            # ex: left section = s[:l] + s[l + 1] and right section = s[:r] + s[r + 1:]
            # this considers all characters apart from the current one and we can check whether either of the substrings given by these strings are palindromes since they involve one of the characters having been deleted

    return True # at this point we have iterated thru the whole string and haven't found a single non-matching pair of characters meaning that the string is a palindrom so we can return true right away


# print(validPalindrome("aba"))
# print(validPalindrome("abca"))
# print(validPalindrome("abc"))