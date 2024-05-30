# 1652

def decrypt(code: list[int], k: int) -> list[int]:
    """
    Time complexity: O(n * k)
        - Outer loop in O(n) time
        - List slicing and calculating sum happens in O(k) time
        - Length calculations happen in O(1) time
        - while loop in the worst case runs O(k) times if curr_len = 0
        - For each iteration, operations inside in the worst case run in O(3k) time which is O(k)
        
    Space complexity: O(n) because `res` grows in size as `code` grows in size
    """
    # All numbers need to be replaced by 0
    if k == 0:
        return [0] * len(code)
    # No matter what k is if the array is of length 1 then there are either enough elements already or 
        # fewer elements than the absolute value of k so we return the array itself
    if len(code) == 1:
        return code

    res = []
    # Case 1: k > 0
    if k > 0:
        for i in range(len(code)):
            start = 0 # we maintain this so that if we don't have enough elements to sum in the forward
                # direction, we loop back from the start to accumulate the remaining elements
            next_k = code[i + 1:i + 1 + k] # extracting the next k elements
            curr_sum = sum(next_k)
            if len(next_k) == k:
                res.append(curr_sum) # we're done here as we've gotten the sum of the next k elements
            else: # loop from beginning of the array
                curr_len = len(next_k)
                # loop from beginning once again adding the current number to the sum until we've summed exactly k elements
                while curr_len < k:
                    curr_sum += code[start]
                    start += 1
                    curr_len += 1
                res.append(curr_sum)
    # Case 2: k < 0
    elif k < 0:
        modified = abs(k) # this is to prevent any indexing issues
        res.append(sum(code[k:])) # handle the sum of the previous k elements for the first element
        for j in range(1, len(code)):
            end = -1
            if j >= modified: # we have atleast k elements before
                res.append(sum(code[j - modified:j]))
            else: # need to loop back from end
                curr, prev_elems = 0, code[:j]
                curr += sum(prev_elems) # accumulate sum of the previous < k elements
                curr_len = len(prev_elems) # this is to maintain number of elements summed
                # loop back from end adding the last element to the current sum and doing so until we've summed abs(k) elements
                while curr_len < modified:
                    curr += code[end]
                    end -= 1
                    curr_len += 1
                res.append(curr)
    
    return res

print(decrypt([5, 7, 1, 4], 3))
print(decrypt([1, 2, 3, 4], 0))
print(decrypt([2, 4, 9, 3], -2))