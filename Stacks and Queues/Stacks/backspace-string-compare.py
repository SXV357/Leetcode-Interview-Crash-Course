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

def more_optimal_solution(s: str, t: str) -> bool:
    # MAIN IDEA
        # WE WANT TO COMPARE ALL THE CORRESPONDING VALID CHARACTERS IN EACH STRING AND AT ANY GIVEN POINT IF ONE PAIR ISN'T EQUAL WE CAN RETURN FALSE BECAUSE IN THE FINAL STRING THE CHARACTERS AT CORRESPONDING INDICES MUST BE EQUAL

    # a b # c
    # a d # c
    def nextValidChar(string, index):
        """
        Main idea:
        - a pound character deletes the character to the left of it so that deleted character is no longer a valid part of the string and we can ignore it but the way we can detect that is through iterating backwards because iterating forward in the string won't give us any information regarding whether this given character needs to be disregarded from the final answer or not

        - what this function does is that given a valid index in both the strings it finds the next valid character in that string and returns that valid characters index. for example if the string was "ab#c", the first valid character is a "c" and then the next valid character is an "a" because when we encounter the first pound, we don't care about what comes to the left of it. 

        - time complexity: O(m + n)
        - space complexity: O(1): MAIN IMPROVEMENT FROM THE LAST SOLUTION WHICH WAS O(m + n) space as well
        """
        num_backspaces = 0 # will keep track of the number of backspaces we've seen so far and critical to determine when we've found the next valid character
        while index >= 0:
            # let's say we have just encountered a backspace and are at a character that isn't a backspace but that means we are not supposed to break out because this character needs to be discarded from the final output. hence if the count of backspaces is 0 and this current one isn't a backspace we've found a valid character and can return
            if num_backspaces == 0 and string[index] != "#":
                break
            # back to before where if we've encountered some number of backspaces and we are at a character that isn't a backspace we decrement the count because we eventually want to go down to the point where we have removed all the characters to be removed via a backspace and are at a valid character
            elif string[index] != "#":
                num_backspaces -= 1
            # as usual incrementing the number of backspaces when we see one 
            else:
                num_backspaces += 1
            # we need to decrement this index because we're iterating backwards thru the string to try and find the next valid character
            index -= 1
        return index
    
    # the actual 2 pointer approach to check all sets of valid characters in both strings
    # we start at the ends of both the strings because we're iterating backwards and trying to compare corresponding sets of characters
    curr_s, curr_t = len(s) - 1, len(t) - 1
    # reason this is the condition is that let's say the length of one string is much smaller than the other causing one to go out of bounds early on and if both the strings' last chars were equal but as a whole deleting all chars which have a pound in front doesn't make them equal, adding the "and" will end up resulting in true which we don't want so as long as one of the indices is in bounds we keep iterating
    while curr_s >= 0 or curr_t >= 0:
        # getting the next valid character in both the strings using the method above
        curr_s = nextValidChar(s, curr_s)
        curr_t = nextValidChar(t, curr_t)

        # since out of bounds situations can be encountered we manually set the characters based on the validity of the updated indices
        s_char = s[curr_s] if curr_s >= 0 else ""
        t_char = t[curr_t] if curr_t >= 0 else ""

        # when we compare the two valid characters and they aren't equal we know the answer is false because this char will be in the final string for both and the strings cannot be equal that way
        if (s_char != t_char):
            return False
        
        # decrement both the indices so we can begin looking for the next set of valid characters and this loop runs until both indices are out of bounds because we want to compare every set of characters. in a way we are implicitly using a 2 pointer approach on strings of equal length given that we continue comparing even when one index goes out of bounds and one doesn't
        curr_s -= 1
        curr_t -= 1

    return True # at the end after we've compared all sets of valid chars in both strings and they all are equal we can simply return true

print(backspaceCompare("ab#c", "ad#c"))
print(backspaceCompare("ab##", "c#d#"))
print(backspaceCompare("a#c", "b"))
print(backspaceCompare("y#fo##f", "y#f#o##f"))