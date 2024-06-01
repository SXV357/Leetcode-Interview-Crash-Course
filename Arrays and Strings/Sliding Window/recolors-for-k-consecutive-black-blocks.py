# 2379

import sys

def minimumRecolors(blocks: str, k: int) -> int:
    # Interpretation
        # In all windows of size k, what is the minimum number of white blocks that exist?

    res = sys.maxsize

    # Original approach

    # for i in range(len(blocks) - k + 1): # O(n - k + 1)
    #     res = min(res, blocks[i:i+k].count("W")) # O(1)

    # Modified sliding window approach

    res = sys.maxsize
    left = num_w = curr = 0

    for right in range(len(blocks)):
        if left > len(blocks) - k:
            break
                
        curr += 1

        if blocks[right] == "W":
            num_w += 1

        if curr == k:
            res = min(res, num_w)
            
        if curr > k:
            if blocks[left] == "W":
                num_w -= 1
            res = min(res, num_w)
            left += 1
            curr -= 1
                
        
    return res

print(minimumRecolors("WBBWWBBWBW", 7))
print(minimumRecolors("WBWBBBW", 2))