from collections import Counter, defaultdict
from typing import List

def twoSum(nums: list[int], target: int) -> list[int]:
    """
    Brute forcing isn't optimal because of input constraints and how for each value we are checking every other value from the next index until the end of the array

    Time complexity: O(n) because we perform a single pass through of the input array with all operations that take place inside happening in constant time(checking existence in hashmap, updating hashmap with new key-value pair)
    Space complexity: O(n) - In the worst case there are no pairs that satisfy the constraint and we end up storing all the elements along with their respective indices in the hashmap
    """

    # hashmap approach
        # the main idea behind this approach is that we store each value in the array along with its corresponding index in the hashmap
        # as we move forward along in the array if we know that we have already stored the complement of the current value in the hashmap we can simply return the value associated with the complement and the current index
        # this cuts down time complexity significantly to O(n) from the brute force solution which is O(n^2)

    seen = {}
    for i in range(len(nums)): # O(n)
        if target - nums[i] in seen: # O(1)
            return [seen[target - nums[i]], i]
        seen[nums[i]] = i
    
    return [-1, -1]

def repeatedCharacter(s: str) -> str:
    """
    Time complexity: O(n) because in the worst case we pass thru all the elements and don't find a single repeating element(all operations inside the loop are taking place in constant time)
    Space complexity: O(n) - in the case where all characters are unique they are stored in the hashmap
    """

    # Set approach(33ms runtime - beats 67.87%)

    # Main idea:
        # we want to find and return the first letter to appear twice so we maintain a set to keep track of this
        # the moment we encounter an element that already exists in the set we know this element has appeared twice and is the first letter so we can return it right array

    # seen = set()
    # for i in range(len(s)):
    #     if s[i] not in seen:
    #         seen.add(s[i])
    #     else:
    #         return s[i]
    
    # Hashmap approach(38ms - beats 29.62%)

    # Main idea:
        # the hashmap is used to store the characters along with their respective frequencies as we traverse the string
        # to avoid key errors when the current character doesn't exist in the hashmap we initialize it to 1
        # if the current character already exists we can simply update its count but an extra step is needed where we immediately check whether its count is greater than 1. if so, we have the first element to appear twice and can return it

    counts = {}
    for i in range(len(s)):
        if s[i] not in counts:
            counts[s[i]] = 1
        else:
            counts[s[i]] += 1
            if counts[s[i]] > 1:
                return s[i]
    
    return ""
    
def findLonely(nums: list[int]) -> list[int]:
    """
    Given an integer array `nums`, find all the unique numbers `x` in nums that satisfy the following: `x + 1` is not in `nums`, and `x - 1` is not in `nums`
    Time complexity: O(n) - for building up the dictionary of frequencies and for iterating over the entire array to check for the conditions
    Space complexity: O(n) - when there are no duplicates and all values are unique we have an entry for every single character in the dictionary
    """

    # The code segment below that updates frequency of all elements in the array has a runtime of 950ms(beats 41.25%)
    # count = {}
    # for i in range(len(nums)):
    #     if nums[i] not in count:
    #         count[nums[i]] = 1
    #     else:
    #         count[nums[i]] += 1

    # This uses the counter function to directly calculate frequency of all elements and has a runtime of 903ms(beats 88.13%) - the original code checks whether the character is a key and then adds it to the dictionary but Counter() combines those two into a single operation which helps cut down on time
    count = dict(Counter(nums))

    # Another possible way to cut down runtime is to instead iterate over the keys of the dictionary and check the following:
        # Is the value associated with this key equal to 1?
        # If so, then check whether key + 1 and key - 1 doesn't exist in the dictionary and if true, append this key to the resulting array

    res = []
    for j in range(len(nums)):
        if count[nums[j]] == 1:
            if nums[j] + 1 not in count and nums[j] - 1 not in count:
                res.append(nums[j])
    
    return res

def checkIfPangram(sentence: str) -> bool:
    """
    Time complexity: O(n) since we are converting the string to a set and then calculating its length
    Space complexity: O(n) since the function is creating the set in memory and then using it for purposes of comparison and in the worst case it stores every single character in the string if no duplicates exist
    """
    # return len(Counter(sentence)) == 26 (37ms runtime(beats 45.56%))
    return len(set(sentence)) == 26 # (33ms runtime(beats 73.25%))

def missingNumber(nums: list[int]) -> int:
    """
    Time complexity: O(n) - we iterate over the range n + 1 times but excluding all constants gives O(n)
    Space complexity: O(n) - because we always store n key/value pairs in the hashmap as a result of all values being unique
    """
    # The main idea:
        # We store a hashmap beforehand so that when iterating over all numbers in the range [0, n] we can check the existence of the values as keys in the dictionary in O(1) time thus cutting down runtime
        # the brute force time consuming approach would be to iterate over all values in the range and for each value check its existence in the array but checking existence in an array is O(n) so the complexity becomes O(n^2)

    freq = Counter(nums)
    res = None

    for i in range(len(nums) + 1):
        if i not in freq:
            res = i
            break

    return res

    # O(1) space solution takes advantage of the fact that we can simply get the sum of the actual n elements and what's in the array and return the difference since that will give the missing value
        # if n = 3, the actual sum would be 0 + 1 + 2 + 3 = 6 and if the array only has [3, 0, 1] which has a sum of 4 we can return 6 - 4 = 2 which is the missing value

def counting_elems(arr: list[int]) -> int:
    """
    Time complexity: O(n) - in the case where there are no duplicates in the array we iterate through freq n times
    Space complexity: O(n) - same as above where if no duplicates exist we store n key-value pairs in the dictionary(if we exclude freq then the SC is O(1) but freq is essential for the function hence we include it)
    """
    freq = Counter(arr)
    res = 0 # this keeps track of how many elements in arr exist such that its next greater element also exists in arr

    # since we need to count duplicates as well and the hashmap only stores unique key-value pairs, if we search freq for the next greater element and find it, we can simply update the count by incrementing it by the element's frequency
        # for ex if we had [1, 1, 2] then the dictionary would be {1: 2, 2: 1}
        # when looping over the keys [1, 2] we see that 2 exists in the dictionary as well, but since it applies for the other 1 as well we increment res by 2 to account for both directly
        # there's no need to check if the next greater element is in the array since all the unique values in the array will be keys in the dictionary
    for k in freq.keys():
        if k + 1 in freq:
            res += freq[k]
    
    return res

def k_distinct(s: str, k: int) -> int:
    """
    You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.
    Time complexity: O(n) - amortized run time and also take into account fact that all the operations happening
    inside the main loop and while loop run in constant time
    Space complexity: O(n) since if there's only one occurrence of every single character we store n keys in freq
    """
    freq = {} # this is used to store frequency of characters in the input string
    left = res = 0 # left pointer and variable to keep track of longest substring
    for right in range(len(s)):
        # the logic here is just to update dictionary with character frequency
        # the check for the existence of the key is necessary since we're working with a normal dictionary
            # that will throw a key error if the key doesn't exist as opposed to defaultdict
        if s[right] not in freq:
            freq[s[right]] = 1
        else:
            freq[s[right]] += 1
        # since the condition is to have k unique characters and dictionaries only store unique keys
        # we can check for the condition being violated when the number of keys exceeds k
        while len(freq) > k:
            freq[s[left]] -= 1 # first decrement the count of the element at the left pointer
            # check if its zero because if it is we can just delete the entire key/value pair from the dictionary
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1
        res = max(res, right - left + 1) # updating length of longest substring now that we have a valid window
    
    return res

def intersection(nums: List[List[int]]) -> List[int]:
    # Brute force solution
        # checks whether for each unique character in the first subarray whether it appears in all the subsequent
        # subarrays then updating result array with that value
    res = []
    for i in range(len(nums[0])):
        curr = nums[0][i]
        count = 0
        for j in nums[1:]:
            if curr in j:
                count += 1
        
        if count == len(nums) - 1:
            res.append(curr)
    
    return sorted(res)

    # Set solution
        # converts all subarrays into sets then takes the intersection of all of them

    # nums = [set(i) for i in nums]
    # return list(sorted(set.intersection(*nums)))

print(intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))
print(intersection([[1,2,3],[4,5,6]]))