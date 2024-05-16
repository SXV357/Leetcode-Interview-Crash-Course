# APPROACHES INVOLVING A SINGLE ITERABLE

def check_if_palindrome(s: str) -> bool:
    """
    Time complexity: O(n) - The while loop can iterate n times at most since the pointers start at distance of n. Work done inside the while loop is O(1) since only comparisons and variable updates are being done maintaining the overall complexity.
    Space complexity: O(1) - Always using only 2 pointer variables no matter what the input is(Start and end of input)
    """
    # initialize a pointer to start at the leftmost index and one at the rightmost index
    left, right = 0, len(s) - 1
    while left < right:
        # a palindrome reads the same forward and backward so at each iteration check whether the
        # characters at both indices are the same
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            # there's a mismatch and it cannot be a palindrome so return false
            return False
    # at this point, the corresponding characters at both indices are equal and both the pointers 
    # have crossed each other so the string must be a palindrome
    return True

def two_sum_modified(nums: list[int], target: int) -> bool:
    left, right = 0, len(nums) - 1 # initializing both the pointers as usual
    """
    Key: The array is sorted now so we can perform a modified binary search
    Time complexity: O(n) - the while loop iterates n times at most and all operations taking place inside the while loop are all constant(arithmetic operation + comparison) 
    Space complexity: O(1) - Still using only two pointers to handle this problem with no additional memory
    """
    while left < right:
        curr_sum = nums[left] + nums[right]
        # if the sum of elements at both the indices is less than the actual one, the leftmost element being added to the rightmost element is too small to contribute to the sum so we increment the left pointer to go to the next bigger element
        if curr_sum < target:
            left += 1
        # if the sum of elements at both the indices is greater than the actual one, the rightmost element being added to the leftmost element is too big to contribute to the sum so we decrement the right pointer to go to the previous smaller element
        elif curr_sum > target:
            right -= 1
        # we have now found two elements which when added together sum to target so return True
        else:
            return True
    # iterated through the entire array until the pointers crossed and didn't find any elements at all so the two pairs of elements don't exist
    return False

# APPROACHES INVOLVING MORE THAN ONE ITERABLE AS PART OF THE INPUTs
def combine_arr(arr1: list[int], arr2: list[int]) -> list[int]:
    """
    Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted
    Both arrays are sorted so we can use a 2 pointer approach to combine both the arrays
    Time complexity: O(n + m) where n = len(arr1) and m = len(arr2). Inside all while loops only O(1) operations are taking place so the complexity is maintained and doesn't increase
    Space complexity: O(1) - Only using 2 pointers as usual exclusing the output array which is not counted
    """
    res = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        # If the resulting array needs to be sorted, then we can compare elements at the corresponding indices in both arrays and add the smaller element first to the list
        if arr1[i] < arr2[j]:
            res.append(arr1[i])
            # Increment only the first pointer because we want to maintain a sorted array even till the end
            i += 1
        # Also handle the case where the element in the first array is greater than the one in the second
        elif arr1[i] > arr2[j]:
            res.append(arr2[j])
            j += 1
        elif arr1[i] == arr2[j]:
            # If we find a match increment both the pointers because we want to run the comparisons on the next set of elements once again
            res.append(arr1[i])
            res.append(arr2[j])
            i += 1
            j += 1
    
    # Example: [1, 2, 3, 4] [3, 5, 8, 9]
        # 1 < 3 - True: Append 1 to the resulting list and increment first pointer
        # 2 < 3 - True: Append 2 to the resulting list and increment first pointer again
        # 3 == 3 - True: Append both the 3's to the resulting list and increment both pointers
        # ...
        # 4 < 5: True so append 4 to the resulting list and break out since the first pointer has reached the end of the list
        # Now only 5, 8, and 9 are pending to be added so add them all to the list and we get [1, 2, 3, 3, 4, 5, 8, 9]
    
    # Cases to handle if any missing elements that need to be added(exhausting both the lists)
    while i < len(arr1):
        res.append(arr1[i])
        i += 1

    while j < len(arr2):
        res.append(arr2[j])
        j += 1

    return res

def isSubsequence(s: str, t: str) -> bool:
    """
    Time complexity: O(n + m) - the pointers cannot move a distance of more than n + m across both the strings
    Space complexity: O(1) - only using 2 pointers and no additional memory
    """
    i = j = 0
    while i < len(s) and j < len(t):
        # Subsequence if all the characters of s appear in t and also in same order. If we're able to match all the characters in s to a character in t it means that we have exhausted all possibilities and s is a subsequence
        # Ex: abc, ahbgdc
            # a == a - True: Now move both the pointers one step forward
            # b != h so keep moving the pointer along t since we want to find a match for b
                # Notice that if b did not exist in t then we would never move the pointer along s and would completely exhaust all the characters in t, meaning that at the end i < len(s) and s is not a subsequence
            # Increment left pointer and b == b so move to the next character in s and next character in t
                # we see that c != g and c != d, so skip those two characters in t and move to the last character in t
            # c == c and we've reached the end of both strings and have also looked at including found a match for all characters in s in t in the same order so s is a subsequence of t
        if s[i] == t[j]:
            # If we find a match, we want to move to the next respective elements since we want to match each character in s exactly once with a character in t
            i += 1
            j += 1
        else:
            # Keep moving along t until we find a match for the current character in s, else the first pointer stays where it is and the second pointer moves through all characters in t until all are visited
            j += 1
    
    return i == len(s)

def reverseString(s: list[str]) -> None:
    """
    Time complexity: O(n) - The two pointers start at a distance of n from each other and move towards each other until they both cross
    Space complexity: O(1) - Using just 2 pointers and no additional memory
    """
    i, j = 0, len(s) - 1
    while i < j:
        # Since we want to reverse the elements in the array, we can just swap the elements at both the pointers and move them both inwards. We keep repeating this process until both the pointers cross each other at which point all elements have been reversed

        s[i], s[j] = s[j], s[i] # Straightfoward way of swapping

        # Another swapping method
        # temp = s[i]
        # s[i] = s[j]
        # s[j] = temp

        i += 1
        j -= 1
    
def sortedSquares(nums: list[int]) -> list[int]:
    """
    Trivial solution time complexity: O(nlogn) - Squaring all elements(n) and sorting(nlogn) and nlogn dominates
    Time complexity: O(n)
    Space complexity: Using 2 pointers for initially populating the result array with the squares and using two additional pointers to sort the resulting array so still O(1)
    """
    # Trivial nlogn solution
    # return sorted(list(map(lambda x: x ** 2, nums)))

    # O(n) 2-pointer solution
    res = []
    l, r = 0, len(nums) - 1
    # Main idea:
        # Since the input array is already sorted and can also contain negative elements, if we are squaring each element it doesn't matter since the squares of all negative numbers are positive
        # We can compare the absolute value of the elements at both pointers and add the square of the element which is greater to the end of the resulting array since we want the resulting array to be sorted as well
    while l <= r: # O(n)
        # If the value on the right is greater, its square must also be greater and since the input array is already sorted this is the largest square so it will be added to the end of the resulting array; now that we have looked at the rightmost element, we can move to the previous one and discard it
        if abs(nums[l]) < abs(nums[r]):
            res.append(pow(nums[r], 2)) # O(1)
            r -= 1
        # If the value on the left is greater, it has the next greatest square so it is added in reverse order to the list from the end and now that we have looked at this element, we can move to the next one and discard it
        else:
            res.append(pow(nums[l], 2)) # O(1)
            l += 1
    
    # Logic here to sort the array of squares since they were all just appended to the array without being added in reverse order from the end(not necessary as the logic to add elements in the appropriate order to the resulting array can be handled in the previous block itself)
    ml, mr = 0, len(res) - 1
    while ml < mr: # O(n)
        res[ml], res[mr] = res[mr], res[ml] # O(1)
        ml += 1
        mr -= 1
    
    return res

def reverseWords(s: str) -> str:
    """
    Time complexity: O(n)
    Space complexity: O(n) - Array to store all the words in the input string and then modifying and returning it
    """
    # Trivial approach:
        # Convert the string into an array - O(n)
        # Reverse each word in the array using two pointer approach - O(n^2)
        # Join everything back into a string and return it - O(n)
        # OVERALL TIME COMPLEXITY: O(n^2)

    # MODIFIED APPROACH TIME COMPLEXITY: O(n)
    words = s.split(" ") # O(n)
    for i in range(len(words)): # O(n)
        words[i] = words[i][::-1] # Assignment = O(1), Reversal: O(n)s
    return " ".join(words) # O(n)

def reverseOnlyLetters(s: str) -> str:
    """
    Time complexity: O(n) - Creating an array consisting of all characters of the string, followed by the while loop iterating over all elements in the array and then joining all the characters back into the final string
    Space complexity: O(n) if we include the char array else O(1) since we're using just 2 pointers
    """
    chars = [char for char in s] # O(n)
    l, r = 0, len(chars) - 1
    while l < r: # O(n)
        l_alpha, r_alpha = chars[l].isalpha(), chars[r].isalpha()
        # All operations here are O(1) - Comparisons and assignments
        if l_alpha and r_alpha:
            chars[l], chars[r] = chars[r], chars[l]
            l += 1
            r -= 1
        else:
            if not l_alpha:
                l += 1
            elif not r_alpha:
                r -= 1
    return "".join(chars) # O(n)

def getCommon(nums1: list[int], nums2: list[int]) -> int:
    # Trivial approach:
        # Convert both arrays into sets to get their intersection
        # Covert the intersection set back into an array and return the smallest element
    
    # Approach 1
    intersection = set(nums1).intersection(set(nums2))
    return min(list(intersection))

    # 2-pointer approach(try to make this work) **
    # res = []
    # i = j = 0
    # while i < len(nums1) and j < len(nums2):
    #     if nums1[i] != nums2[j]:
    #         i += 1
    #     else:
    #         res.append(nums1[i])
    #         i += 1
    #         j += 1
    
    # return min(res)

# print(getCommon([1,2,3,6], [2,3,4,5]))
# print(getCommon([1,2,3], [2, 4]))

def moveZeroes(nums: list[int]) -> None:
    # base cases(just one element)
    pass