# 1475

def finalPrices(prices: list[int]) -> list[int]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    res = [0] * len(prices)
    stack = []
    for i, price in enumerate(prices):
        # logic to maintain a strictly monotonically increasing stack
        while stack and price <= prices[stack[-1]]:
            idx = stack.pop()
            res[idx] = prices[idx] - price
        stack.append(i) # reason we store indices is so that when we encounter the next <= element for the current element, we can simply update that corresponding element's index in the resulting array by accessing the element present at that index
    
    # some elements in the array may not have a next <= element but we would have those elements' indices in the stack, so we add the elements in the array pointed to by those indices to the resulting array
    while stack:
        modified = stack.pop()
        res[modified] = prices[modified]
    
    return res

print(finalPrices([8,4,6,2,3]))
print(finalPrices([1,2,3,4,5]))
print(finalPrices([10,1,1,6]))