#946

def optimal_solution(pushed: list[int], popped: list[int]):
    """
    Time complexity: O(n) amortized
    Space complexity: O(n)
    """
    # the main idea behind this solution is that we keep appending elements to the stack until we encounter a situation where the topmost element is equal to the element at the index pointed to by the pointer in popped. from where we keep popping elements until this condition is violated and at the end if all the pushing and popping operations were valid we will end up with an empty stack
    i = 0
    stack = []
    for el in pushed:
        stack.append(el)
        while stack and stack[-1] == popped[i]:
            stack.pop()
            i += 1
    
    return not stack

def validateStackSequences(pushed: list[int], popped: list[int]) -> bool:
    """
    Time complexity: O(n^2) because for each iteration we're checking whether the current element is in the stack or not
    Space complexity: O(n) to store the hashmap mapping the values to their indices for pushed
    """
    # if the arrays are already equal we can push one element and pop one element until the end
    # if one is the reverse of the other, then we can push everything first then pop everything one by one
    if pushed == popped or popped == pushed[::-1]:
        return True
    
    stack = []
    freq = {val: i for i, val in enumerate(pushed)} # to keep track of the indices of all values in pushed
    start = 0 # this will be used to keep a track of the index after which new elements will be pushed onto the stack following some element which wasn't seen before

    for el in popped:
        idx = freq[el] # this element's index in the pushed array
        i = start
        if el not in stack:
            # if we haven't seen this value in the stack yet, we keep looping adding all elements to the stack until we add this element which we haven't seen yet
            while i <= idx:
                stack.append(pushed[i])
                i += 1

            # reason we update this within this block is that if there are any remaining elements which can be added and popped they wont get accounted for
            start = idx + 1

        # makes sense to only pop the element if it matches the current element in the popped array
        if stack and stack[-1] == el:
            stack.pop()
    
    # if we have pushed all elements and have popped them the stack will be empty and we can check for that at the end
    return not stack

print(validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))
print(validateStackSequences([1,2,3,4,5], [4,3,5,1,2]))
print(validateStackSequences([4,0,1,2,3], [4,2,3,0,1]))
print(validateStackSequences([2,1,0], [1,2,0]))