# 739

def dailyTemperatures(temperatures: list[int]) -> list[int]:
    """
    Brute force time complexity: O(n^2)
    Optimal solution time complexity: O(n) amortized and O(n) space time complexity to store the answer array

    COME BACK TO THIS LATER TO RE-ATTEMPT
    """
    # res = []

    # Brute force solution - TLE
    # for i in range(len(temperatures)):
    #     num_days = 0
    #     j = i + 1
    #     curr_max = temperatures[i]
    #     while j < len(temperatures):
    #         if temperatures[j] > temperatures[i]:
    #             num_days += 1
    #             curr_max = max(curr_max, temperatures[j])
    #             break
    #         else:
    #             num_days += 1
    #         j += 1
        
    #     if curr_max == temperatures[i]:
    #         res.append(0)
    #     else:
    #         res.append(num_days)

    # alternate solution(attempt at using a stack) - TLE

    # stack = []
    # for i in range(len(temperatures)):
    #     j = i + 1
    #     stack = []
    #     if not j > len(temperatures) - 1:
    #         stack.append(temperatures[j])
    #     while stack and stack[-1] <= temperatures[i]:
    #         j += 1
    #         if j == len(temperatures):
    #             break
    #         stack.append(temperatures[j])

    #     if stack and not stack[-1] > temperatures[i]:
    #         res.append(0)
    #     else:
    #         res.append(len(stack))

    # optimal solution using a monotonic decreasing stack

    ans = [0] * len(temperatures) # this array will be used to store the result
    stack = [] # the stack which will be used to process elements in the temperatures array
    
    # main idea:
        # at any given time in the stack we are storing elements for which we haven't found a warmer temperature, i.e, if there's a sequence of consecutively decreasing elements then those don't have a warmer temperature yet to be found so if we maintain a monotonic decreasing stack we can use it to detect when we find the first warmer temperature because it would mean that it is warmer than the last element in the stack and potentially ones before it
        # let's say the array is [40, 35, 32, 37, 50] for which the result is [4, 2, 1, 1, 0]
        # the first three elements are in decreasing order and we can add them to the stack and so far we haven't found a warmer temperature than any of them
        # once we hit 37 the decreasing condition is violated so we can keep popping elements off the stack until they're in decreasing order again but at the same time we can update the distance from the popped elements to the current element because as long as they're lesser than the current one this current element is the next warm temperature
        # the stack essentially stores the indices of the visited elements and once we encounter an element that breaks the decreasing sequence, we update the distances as well as pop elements off the stack until the condition is satisfied once again

    for i, v in enumerate(temperatures):
        # as long as this element is greater than the last seen element in the stack we pop the last element off the stack and update the distance from the popped element to this one because its the closest warmer temperature
        while stack and v > temperatures[stack[-1]]:
            ans[stack[-1]] = i - stack[-1]
            stack.pop()
        # once the decreasing order condition is no longer violated we add the current element and repeat once again
        stack.append(i)

    return ans

print(dailyTemperatures([73,74,75,71,69,72,76,73]))
print(dailyTemperatures([30,40,50,60]))
print(dailyTemperatures([30,60,90]))