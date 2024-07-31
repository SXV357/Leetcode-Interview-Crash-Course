#2390

def removeStars(s: str) -> str:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    stack = []
    # main idea is that we need to delete the characters to the left of a star so we can use a stack
        # when we encounter a star we pop the top element off the stack but if we dont we simply append it to the stack
    for c in s:
        if c != "*":
            stack.append(c)
        elif stack:
            stack.pop()
    
    return "".join(stack)

print(removeStars("leet**cod*e"))
print(removeStars("erase*****"))