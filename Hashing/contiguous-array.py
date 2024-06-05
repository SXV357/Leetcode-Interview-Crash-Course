# 525

def findMaxLength(nums: list[int]) -> int:
    """
    Come back to this to re-attempt tomorrow
    """
    # Brute force solution - TLE

    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         curr = nums[i:j+1]
    #         if curr.count(0) == curr.count(1):
    #             res = max(res, len(curr))

    # The brute force solution involves exploring all subarrays of nums and checking whether the number of 0's 
    # and 1's is equal for all of them and accordingly updating the answer but this is an O(n^2) solution
    # Ideally for such problems, sliding window can be used but here there isn't a clear cut way or logic to 
        # shrink the window based on some predetermined condition. We could keep expanding the window accumulating
        # the sum of number of 0's and 1's and ideally if by the time we reach the end of the array and the counts are equal then we have found the largest subarray but what if that's not the case then we're stuck
    
    # The solution involves a hashmap with a modified prefix sum approach

    # In the ideal case the largest subarray that satisfies the constraints would start at index 0 and end at len(nums) - 1 but that need not always be the case because the largest one could
        # a) start at index 0 and end at some index before len(nums) - 1
        # b) start at some index after 0 and end at len(nums) - 1
        # c) start at some index after 0 and end at some index before len(nums) - 1

    dic = {} # the way we will approach this problem is by mapping the difference of the number of one's and zero's 
    # to the ending index because the ending index will eventually help us figure out the length of the largest subarray

    # zero and one are used to keep track of the number of 0's and 1's encountered so far up to the current index
    # and res is used to keep track of the length of the largest subarray
    zero = one = res = 0
    for i in range(len(nums)):
        # the logic below is for updating the number of 0's and 1's
        zero += (nums[i] == 0)
        one += (nums[i] == 1)

        # this is where we create the key/value pair of the count difference and the current index
        if one - zero not in dic:
            dic[one - zero] = i
        
        # in the case where the counts are equal which is what we want the length would just be the sum
        # NOTE: this need not occur just from 0 -> len(nums) - 1 but anywhere else but at this time it is the largest
            # and is subject to change in the future as we iterate through the array
        if one == zero:
            res = one + zero
        # ex: 1 1 1 0 0
        # here the largest subarray that has equal counts is 1 1 0 0 with a length of 4
        # iterating through the array we store the following in the hashmap until index 2: {1: 0, 2: 1, 3: 2}
        # now at index 3 when we encounter a zero for the very first time, the difference between number of one's and 
            # zero's is 2 which has already been seen in the hashmap where we have a surplus of 1's at index 1
            # we don't want to lose that previous information but also know that the counts aren't equal where 0 appears once and 1 appears thrice
            # however we know that [1, 0] is a valid subarray that satisfies this of length 2. we are currently at index 3 and the last index where we observed the difference was 1 and 3 - 1 = 2
            # this works because if we delete the first two 1's we are left with [1, 0] which works
            # similarly we eventually get 2 0's and 3 1's with a difference of 1 and it was there at index 0 and taking the difference gives 4 - 0 = 4 which relates to [1, 1, 0, 0] that forms a valid subarray
        
        # DOING "i - dic[one - zero]" ESSENTIALLY GIVES US THE LENGTH OF THE LARGEST SUBARRAY THAT CAN BE OBTAINED BY DELETING CERTAIN ELEMENTS FROM THE LEFT WHICH SATISFIES THE CONDITIONS IN THE PROBLEM
        else:
            res = max(res, i - dic[one - zero])
    
    return res

print(findMaxLength([0,1]))
print(findMaxLength([0,1,0]))