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
    """
    Approach 1: Brute force solution
    - TC: `O(m * n^2 + mlogm)` - let's assume the length of nums[0] is `m` and the average length of all arrays after the first one is `n`. for the remaining `n - 1` arrays we are checking existence of a value which takes `O(n)` time hence we have the first part which is `m * n^2`. Then the sorting at the end also takes time and its `mlogm` because in thw worst case all the `m` elements in `nums[0]` appear in all the remaining `n - 1` arrays.
    - SC: `O(m)` because the only data structure we're using that scales with input size is `res` and in cases where all the elements of `res` appear in all the other arrays we end up storing `m` elements overall
    
    Approach 2: Set solution
    - TC: `O(n^n + nlogn)` - converting all the subarrays of `nums` into a set takes O(n^2) time because we are iterating over each subarray and converting it into a set which takes O(n) time. For the second part, the complexity of the set intersection of all elements of `nums` is `O(n^n)` since the intersection method in the worst case takes `O(len(s_1) * len(s_2) * ... * len(s_n))` where `s_1 .... s_n` are the sets being intersected. We have `n` sets and assuming each set has an average length of `n` that's how we get `n^n`. Finally sorting the result takes `O(nlogn)` time since in the worst case all the elements of one subarray appear in all the other ones thus resulting that time complexity.
    - SC: `O(n)` because as `nums` grows in size the number of set conversions and storage also increases
    """

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

    # nums = [set(i) for i in nums] - O(n^2)
    # return list(sorted(set.intersection(*nums))) - O(n^n + nlogn)

def areOccurrencesEqual(s: str) -> bool:
    """
    Time complexity: O(n) - the list to set conversion including calculating the length of the set in the worst case takes place in linear time since we would be storing every single character in the hashmap if everything was unique
    Space complexity: O(n) - in the worst case all characters are unique so we store `n` entries in the hashmap
    """
    occurrences = Counter(s)
    # if all the characters appear the same number of times the values array will only contain one kind of value and if we convert that into a set we can check if its length is equal to 1 because that would mean there's only one unique value
    return len(set(occurrences.values())) == 1 # 29ms runtime(beats 95.28%)

    # 42ms runtime(beats 33.44%)
    # keys = list(occurrences.keys())
    # for i in range(len(keys) - 1):
    #     if occurrences[keys[i]] != occurrences[keys[i + 1]]:
    #         return False
    
    # return True

# APPLICATION OF HASHING TO SLIDING WINDOW PROBLEMS WHERE A MORE STRICTER CONSTRAINT EXISTS AND FOR WHICH THE STANDARD WINDOW EXPANSION AND SHRINKING WON'T WORK

def subarraySum(nums: List[int], k: int) -> int:
    """
    Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.
    Time complexity: O(n) because we always iterate through every single element of `nums` and then perform the remaining operations
    Space complexity: O(n) because in the case where we have only positive values in the array the accumulating prefix will always keep increasing and we will store `n` unique keys in the hashmap
    """

    # Main idea:
        # In this approach we store the frequencies of prefix sums in the input array because that will be used to update how many subarrays end at a specific index i with a sum equal to k
        # what we do is to maintain a variable to keep a track of the current prefix sum and storing it in the hashmap at each step of the iteration
        # the way we determine if we have reached an index i that forms a subarray with sum equal to k is to check whether we have already observed the prefix sum of curr - k in the hashmap
            # let's say the input is [1, 2, 3] and it has a prefix of [1, 3, 6] with k = 3
            # one thing we need to make sure to do is to account for the fact that an empty subarray has a sum of 0 and to begin with it occurs only once so we create that key/value pair in the hashmap initially
            # the prefix at index 0 is 1 and ideally if this subarray which contains just one element had a sum of k then this value - k = 0 and we check if 0 exists in the hashmap which it does since we already initialized it, however 1 - 3 = -2 doesn't exist in the hashmap as a key so this subarray doesn't have a sum equal to k
            # now we move to index 1 and accumulate a prefix sum of 3 and we check whether currPrefix - k = 0 exists in the hashmap which it does so we increment the number of matched subarrays by the frequency associated with the prefix of an empty subarray and this logic carries over for all indices

    prefix = defaultdict(int)
    prefix[0] = 1 # this is needed because if we don't account for this then we miss counting certain valid subarrays
    # curr is used to store the current prefix up to index i and res is used to keep track of number of subarrays with sum equal to k
    curr = res = 0  
    for i in nums:
        curr += i
        # since we're using a defaultdict object there's no need to check if the key exists because no key errors will be thrown. if the key doesn't exist the default int value which is 0 will be added to res
        if curr - k in prefix:
            res += prefix[curr - k]
        prefix[curr] += 1
    
    return res

def numberOfSubarrays(nums: List[int], k: int) -> int:
    """
    Time complexity: O(n) since we are iterating through the entire input array and updating hashmap at the same time
    Space complexity: O(n) - if no duplicate prefixes exist then we store `n` unique keys in the hashmap
    """
    # brute force solution - TLE

    # res = 0
    # for i in range(len(nums)):
    #     if k == 1 and nums[i] % 2 != 0:
    #         res += 1
    #     for j in range(i + 1, len(nums)):
    #         n_odd = 0
    #         curr = nums[i:j + 1]
    #         for val in curr:
    #             n_odd += 1 if val % 2 != 0 else 0
    #         if n_odd == k:
    #             res += 1
    
    # return res
    
    count = defaultdict(int) # this will store the number of odd numbers as the key and the number of subarrays containing those many odd numbers as the value
    count[0] = 1 # this is necessary and basically indicates that there is one subarray to begin with that has 0 odd numbers which is the empty subarray
    
    res = curr = 0 # res keeps track of number of valid subarrays and curr keeps track of number of odd elements so far
    for j in nums:
        curr += 0 if j % 2 == 0 else 1 # we can technically just do curr += j % 2 since the modular div returns 1 if the number is odd and even otherwise
        res += count[curr - k] # as of this index, curr represents the number of odd numbers we've seen till here and if curr - k exists it means that there was another subarray previously with those many odd numbers and the difference between the two results in k odd numbers being present between both the indices
        count[curr] += 1 # this is for updating the hashmap with the number of odd numbers and number of subarrays that satisfy them
    
    print(dict(count))
    
    return res