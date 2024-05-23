# 2269

def parse_substring(s: str) -> bool:
    """
    Time complexity: O(n)
    """
    return int(s) != 0

def divisorSubstrings(num: int, k: int) -> int:
    """
    Time complexity:
    Space complexity: 
    """

    # APPROACH 1(39 ms runtime)

    # res = 0
    # initial_k = str(num)[:k]
    # if parse_substring(initial_k):
    #     if num % int(initial_k) == 0: 
    #         res += 1
    
    # modified_num = str(num)
    # for i in range(1, len(modified_num)):
    #     curr = modified_num[i:i + k]
    #     if len(curr) == k:
    #         if parse_substring(curr) and num % int(curr) == 0:
    #             res += 1
    
    # return res

    # APPROACH 2(37 ms runtime)

    left = res = curr = 0
    modified = str(num)
    for right in range(len(modified)):
        curr += 1
        while curr > k:
            curr -= 1
            left += 1
        if curr % k == 0:
            substr = modified[left:right + 1]
            if parse_substring(substr) and num % int(substr) == 0:
                res += 1
        
    return res          

print(divisorSubstrings(240, 2))
print(divisorSubstrings(430043, 2))
print(divisorSubstrings(30003, 3))