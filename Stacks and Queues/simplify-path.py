# 71

def simplifyPath(path: str) -> str:
    """
    Time complexity: O(n) 
    - Replacing all instances of the target string in the original one with the modified one - O(n)
    - Splitting the string based on the / delimiter - O(n)
    - Iterating over all elements of the split string - O(n)
    - Concatenating all elements in the stack at the end - O(n)
    Space complexity: O(n) to hold the stack because it grows in size as the original input string grows in size
    """
    path = path.replace("//", "/") # preprocess the string by replacing all double slashes with a single one(technically not needed because when we split the string larger groups of slashes apart from 2's will become empty strings which we just ignore when iterating)
    elems = path.split("/") # to access the directory names as well as any upper directories

    # not needed either because we ignore all empty strings when iterating through the split array
    if elems[-1] == "":
        elems.pop()

    stack = [] # the stack will store the canonical path from the source directory to the destination directory
    for el in elems:
        # if we encounter a ".." it means we move up a directory so we delete the last seen directory from the stack
        if stack and el == "..":
            stack.pop()
        else:
            # in all other cases we ignore the following characters and only add the valid directories to the stack
            if el != "." and el != ".." and el != "":
                stack.append(el)
    
    # the whole part below is not needed since we can simply concatenate the elements in the stack with a "/" and prepend a "/" at the beginning as per question requirements
    if stack:
        modified = "/".join(stack)
        if not modified.startswith("/"):
            modified = "/" + modified
        return modified
    
    return "/"

print(simplifyPath("/home/../../.."))
print(simplifyPath("/a//b////c/d//././/.."))
print(simplifyPath("/home/"))
print(simplifyPath("/home//foo/"))
print(simplifyPath("/home/user/Documents/../Pictures"))
print(simplifyPath("/../"))
print(simplifyPath("/.../a/../b/c/../d/./"))
print(simplifyPath("/a/../../b/../c//.//"))
print(simplifyPath("/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///"))