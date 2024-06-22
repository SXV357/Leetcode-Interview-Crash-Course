# 844

def backspaceCompare(s: str, t: str) -> bool:
    """
    Time complexity: O(m + n) because we iterate over each string separately to handle the backspaces followed by concatenating all the characters back together at the end
    Space complexity: O(m + n) because as both the strings grow in size the stacks will also grow in size
    """
    # the main idea is that whenever we encounter a "#" in the string we need to get rid of the character to the left of it if at all there exists one and this is a perfect use case for a stack because the last character appearing before a hashtag would be the last element pushed onto the stack and we can simply pop that character off and continue
    # we handle this separately for both the strings since they could be of different lengths and once we've handled all backspaces we can compare the two strings to see if they're equal

    # handle deleting all characters preceding a backspace in s
    s1 = []
    for char in s:
        if s1 and char == "#":
            s1.pop()
        else:
            if char != "#":
                s1.append(char)
    
    # handle deleting all characters preceding a backspace in t
    t1 = []
    for char in t:
        if t1 and char == "#":
            t1.pop()
        else:
            if char != "#":
                t1.append(char)
    
    # check if both strings are the same at the end after the deletion has been done
    return "".join(s1) == "".join(t1)

print(backspaceCompare("y#fo##f", "y#f#o##f"))
print(backspaceCompare("ab#c", "ad#c"))
print(backspaceCompare("ab##", "c#d#"))
print(backspaceCompare("a#c", "b"))