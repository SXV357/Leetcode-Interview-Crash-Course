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
    """

    # Brute force
    count = {}
    for i in range(len(nums)):
        if nums[i] not in count:
            count[nums[i]] = 1
        else:
            count[nums[i]] += 1

    res = []
    for j in range(len(nums)):
        if count[nums[j]] == 1:
            if nums[j] + 1 not in count and nums[j] - 1 not in count:
                res.append(nums[j])
    
    return res

