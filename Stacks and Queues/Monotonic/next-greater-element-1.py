# 496

def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Time complexity: O(`len(nums1) + len(nums2)`)
    - O(`len(nums1)`) because of populating the hashmap with all the values and indices
    - O(`len(nums2)`) because we need to iterate over the entirety of nums2 and also update the stack at the same time
    Space complexity: O((2 * `len(nums1)`) + `len(nums2)`)
    - The first part is primarily to store the resulting array as well as the hashmap
    - The second part takes into account the worst case scenario when all the elements in `nums2` are already in decreasing or strictly decreasing order
    """
    res = [-1] * len(nums1) # this array will store the next greatest element for values in nums1 that are in nums2
    # the hashmap maps the values in nums1 to their indices so that when we find the next greater element for a matched value we can lookup the index and then update the resulting array
    mappings = {v: i for i, v in enumerate(nums1)}

    # main idea: monotonic decreasing stack
    
    stack = []
    for i in range(len(nums2)):
        # since we want to maintain a monotonic decreasing stack, if there's an element we find which is greater then the top of the stack we cannot afford to add that element so we need to keep popping elements off the stack until we get back to maintaining that property
        while stack and nums2[i] > stack[-1]:
            # the extra condition we use here is to check whether the top of the stack is a value that exists in nums1 and if so we lookup the index of that value in nums1 and update the corresponding index in res with the current greatest value we found because it is guaranteed to be the next greater element
            if stack[-1] in mappings:
                res[mappings[stack[-1]]] = nums2[i]
            # in all other cases, no updates needed and we can just pop the element off the top of the stack
            stack.pop()
        stack.append(nums2[i]) # now that we have discarded all unnecessary elements we can add the current element and its guaranteed it will not violate the properties
    
    return res

print(nextGreaterElement([4,1,2], [1,3,4,2]))
print(nextGreaterElement([2,4], [1,2,3,4]))