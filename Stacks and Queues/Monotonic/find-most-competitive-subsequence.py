# 1673

def mostCompetitive(nums: list[int], k: int) -> list[int]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    # main idea: we use a monotonically increasing stack here because we want to return the most competitive subsequence(i.e the subsequence where we have the smallest elements in non-decreasing order)
        # further, here's something else to think about: we want to find the most competitive subsequence of size k but the size of the array could be greater than or equal to k. if its equal to k, we simply return the array as is but in the other case we'll have to delete some elements before we get the right subsequence

    num_del = len(nums) - k # the number of elements to delete from the array to form the subsequence
    stack = [] # the stack which we'll use to hold the subsequence
    for num in nums:
        # check 1: is the next element smaller than the one at the top of the stack? if so, it violates the properties of a monotonically increasing stack and in order to preserve the increasing order we will have to delete some elements.
        # check 2: we can delete the element but we can't delete just any element because we want to make sure that the stack ends up having k elements at the end but since we only have to delete num_del elements once we run out of elements to delete we simply add elements to the stack without doing any sort of popping because any popping beyond that will reduce the size of the stack below the desired value
        while stack and stack[-1] > num and num_del > 0:
            stack.pop()
            num_del -= 1
        stack.append(num)
    
    return stack[:k] # the stack may have >= k elements at the end so just slice out the first k elements and return it

print(mostCompetitive([3,5,2,6], 2))
print(mostCompetitive([2,4,3,3,5,4,9,6], 4))
print(mostCompetitive([71,18,52,29,55,73,24,42,66,8,80,2], 3))
print(mostCompetitive([84,10,71,23,66,61,62,64,34,41,80,25,91,43,4,75,65,13,37,41,46,90,55,8,85,61,95,71], 24))