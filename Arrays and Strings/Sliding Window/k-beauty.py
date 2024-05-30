# 2269

def parse_substring(s: str) -> bool:
    """
    Time complexity: O(n) because the entire string of size n needs to be converted into an integer
    """
    return int(s) != 0

def divisorSubstrings(num: int, k: int) -> int:
    """
    Time complexity: O(n) - Amortized run time
    Space complexity: O(n) - We are storing a stringified version of the input number and it grows as the number of digits in the number grows
    """

    # APPROACH 1(39 ms runtime) - Standard window of fixed size approach

    # This approach checks the condition for the first k characters and then for subsequent sets of
    # k characters in a loop

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

    # APPROACH 2(37 ms runtime) - Standard algorithm incorporating window of fixed size

    # res is used to keep track of number of valid substrings
    # curr is used to keep track of the current length of the substring
    left = res = curr = 0
    modified = str(num)
    for right in range(len(modified)):
        curr += 1 # we have encountered one character so include it in the current sum
        # this is evaluated once we have included more than k characters
        while curr > k:
            curr -= 1
            left += 1
        # we are calculating the things for substrings of size k so checking if curr is divisible by k helps with that
        if curr % k == 0:
            # extracting the substring
            substr = modified[left:right + 1]
            # 0 cannot divide anything so we check if its not equal to 0 as well as whether the original number is divisible by this substring
            if parse_substring(substr) and num % int(substr) == 0:
                res += 1
        
    return res          

print(divisorSubstrings(240, 2))
print(divisorSubstrings(430043, 2))
print(divisorSubstrings(30003, 3))