# 20

def isValid(s: str) -> bool:
    """
    Time complexity: O(n) because we iterate through all characters of the string and all operations that happen inside are constant time operations
    Space complexity: O(n) because as the string grows bigger the stack also grows bigger even if elements are constantly being pushed and popped
    """
    # map all sets of valid parentheses to their respective counterparts to use for reference
    mappings = {")": "(", "]": "[", "}": "{"}

    stack = [] # stack will be used because the problem follows a LIFO structure where we need to match the last seen open bracket with a closed bracket in the string
    
    # the idea is that if we've successfully matched all sets of parentheses then the stack will be empty and we return true otherwise false since there will be some characters in the stack which haven't been mapped

    for char in s:
        # if we encounter a closing bracket we need to check for a few things
        if char in mappings:
            # if the most recent bracket in the stack is the corresponding opening bracket for this closing bracket then we have matched the first set and can pop the opening bracket from the stack
            if stack and stack[-1] == mappings[char]:
                stack.pop()
            # in the case where the stack is empty or the brackets don't align we just append the closing bracket because it would mean that at the end the stack wouldn't be empty
            else:
                # WE COULD SIMPLIFY THE CONDITION ABOVE TO JUST BE ELSE AND THEN RETURN FALSE HERE BECAUSE
                    # 1. IF WE HAVE A CLOSING BRACKET BUT THE RECENT UNCLOSED OPENING BRACKET IS NOT THE RIGHT ONE THE STRING IS INVALID
                    # 2. IF WE HAVE A CLOSING BRACKET BUT THE STACK IS EMPTY THERE IS NO OPENING BRACKET TO MATCH THIS SO BY DEFAULT THE STRING IS NOT VALID
                return False
        else: # these are all the open brackets so we just push them onto the stack
            stack.append(char)

    return not stack # if we have matched all possible sets of brackets then the stack will be empty otherwise it won't be

print(isValid("()")) # true
print(isValid("()[]{}")) # true
print(isValid("(]")) # false
print(isValid("([)]")) # false
print(isValid("]")) # false
print(isValid("[([]])")) # false
print(isValid("(])")) # false
print(isValid("([}}])")) # false