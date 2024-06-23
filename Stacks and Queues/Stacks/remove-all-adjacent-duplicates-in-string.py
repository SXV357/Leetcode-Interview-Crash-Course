# 1047

def removeDuplicates(s: str) -> str:
    """
    Time complexity: O(n) because we iterate through all characters once to delete the adjacent duplicates and then concatenate all remaining characters together
    Space complexity: O(n) because as `s` grows in size the stack also does
    """
    stack = [] # the stack will be used to hold the current state of the string as the adjacent duplicate removals are done so that by the time we finish iterating through all characters we have the updated string which we can just concatenate together and return

    for c in s:
        # we want to choose adjacent letters and remove them so when we encounter a letter whose duplicate has already been added to the stack before, we can simply pop off that duplicate because it means we have effectively removed this pair
        if stack and stack[-1] == c:
            stack.pop()
        else: # in other cases where there are no adjacent duplicates we keep pushing onto the stack
            stack.append(c)
    
    return "".join(stack) # at the end once we have deleted all adjacent duplicates we can concatenate together all characters of the stack and return it

print(removeDuplicates("abbaca"))
print(removeDuplicates("azxxzy"))