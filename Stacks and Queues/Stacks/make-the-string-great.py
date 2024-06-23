# 1544

# upper case: 65-90
# lower case: 97-122

def makeGood(s: str) -> str:
    """
    Time complexity: O(n) because we need to iterate through the entire string to construct the modified one with all operations that take place inside happening in constant time
    Space complexity: O(n) because the stack grows large as the input string grows large
    """
    stack = [] # this will store the modified characters
    for c in s:
        # condition 1: the characters are the same(i.e, ascii value difference is 32)
        # condition 2: one is lowercase and the other is uppercase and vice versa(this technically doesn't need to be checked since the first condition where we check the ascii difference is enough to determine if they're the same character and one is upper and one is lower)
        if (stack) and (abs(ord(stack[-1]) - ord(c)) == 32 and ((stack[-1].islower() and c.isupper()) or (stack[-1].isupper() and c.islower()))):
            # popping it off the stack is like deleting this pair of characters 
            stack.pop()
        else:
            # in all other cases just add the character to the stack because we haven't found such a pair
            stack.append(c)
    
    return "".join(stack) # at the end concatenate all characters together and return them

assert(makeGood("leEeetcode") == "leetcode")
assert(makeGood("abBAcC") == "")
assert(makeGood("s") == "s")
assert(makeGood("mC") == "mC")
print("All assertions passed")