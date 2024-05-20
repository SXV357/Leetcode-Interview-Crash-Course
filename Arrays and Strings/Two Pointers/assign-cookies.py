# 455

def findContentChildren(g: list[int], s: list[int]) -> int:
    """
    Time complexity: O(max(n log n, m log m)) since the sorting of both arrays overpowers the actual runtime of the while loop which can be either O(n) or O(m) depending on how many times the pointers are moved forward
    Space complexity: O(1) - just using 3 variables and no additional data structures that grow with input size
    """
    max_content = 0 # keep track of maximum number of children satisfied
    # we sort both the arrays because it may be the case that there are cookie sizes which match some entries in the greed list but in a different location
    g.sort()
    s.sort()
    # the pointers below are used to keep track of each entry within both the input lists
    i = j = 0
    # Key: each child can only be assigned a max of one cookie
    while i < len(g) and j < len(s): # depends(could be O(n) or O(m))
        # once we find a valid cookie update number of content children and move both pointers forward because one child can only be assigned a max of one cookie
            # once child i has been assigned cookie j, neither child i nor cookie j can be assigned again to their respective counterparts
        if g[i] <= s[j]:
            max_content += 1
            i += 1
            j += 1
        # if there's a mismatch, we keep moving along the cookie size array to see if we can satisfy this child's greed
        elif g[i] > s[j]:
            j += 1
    
    return max_content

print(findContentChildren([1, 2, 3], [1, 1]))
print(findContentChildren([1, 2], [1, 2, 3]))
