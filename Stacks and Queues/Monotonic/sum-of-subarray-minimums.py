# 907

def sumSubarrayMins(arr: list[int]) -> int:
    # res = 0
    # for i in range(len(arr)):
    #     curr_min = arr[i]
    #     res += curr_min
    #     for j in range(i + 1, len(arr)):
    #         curr_min = min(curr_min, arr[j])
    #         res += curr_min
    
    # return res % (pow(10, 9) + 7)

    # for each number, how many times is this number the minimum of a subarray
        # need to calculate number of subarrays which has this element as a minimum
    
    # monotonically increasing stack
    res, n = 0, len(arr)
    stack = []
    for i in range(len(arr)):
        while stack and arr[i] < arr[stack[-1]]:
            popped_idx = stack.pop()
            left = popped_idx - stack[-1] if stack else popped_idx + 1
            right = i - popped_idx
            res += (arr[popped_idx] * (left * right))
        stack.append(i)
    
    for i in range(len(stack)):
        left = stack[i] - stack[i - 1] if i > 0 else stack[i] + 1
        right = n - stack[i] # the stack is alr in increasing order so to get how many subarrays to the right this elem is a minimum of, just use a reference to the end of the array
        res += (arr[stack[i]] * (left * right))
    
    return res % (pow(10, 9) + 7)