# 345

def reverseVowels(s: str) -> str:
    """
    Time complexity: O(n) - main loop runs n times since the pointers start at a distance of n from each other and keep moving inwards until they cross
    Space complexity: O(n) - to store all characters of s
    """
    # store all vowels in a set for optimization purposes especially when looking up a given element(checking for existence in set is O(1))
    vowels = {'A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u'}
    l, r = 0, len(s) - 1
    chars = list(s) # convert string to list of chars since we cannot swap directly in string
    # main idea: we can only swap if the characters at both indices are vowels
    while l < r:
        # the right char is a vowel so we want to move the left pointer inwards till we can find a vowel at the left index
        if chars[l] not in vowels and chars[r] in vowels:
            l += 1
        # left char is a vowel so we want to move right pointer inwards till we can find a pointer at the right index
        elif chars[l] in vowels and chars[r] not in vowels:
            r -= 1
        # found vowels at both indices so swap the characters and move both pointers inwards
        elif chars[l] in vowels and chars[r] in vowels:
            chars[l], chars[r] = chars[r], chars[l]
            l += 1
            r -= 1
        # none are vowels and we need two vowels to swap so move both pointers inwards
        elif chars[l] not in vowels and chars[r] not in vowels:
            l += 1
            r -= 1
        
    return "".join(chars) # O(n) operation since we're concatenating all elements of the characters list to a string

print(reverseVowels("hello"))
print(reverseVowels("leetcode"))