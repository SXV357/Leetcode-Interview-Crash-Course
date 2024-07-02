# 901

class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        """
        Time complexity: O(1) amortized because the while loop need not necessarily execute for every single value in the stack but at the end averages out to O(1)
        Space complexity: O(n) because the stack could grow to have `n` elements if all the stocks were already in decreasing order to begin with

        COME BACK TO THIS LATER TO RE-ATTEMPT
        """
        # brute force solution
            # the solution below by itself is O(n) in the worst case but for how many ever calls are made to this function, its actual worst case run time is O(n^2)
            # lots of recalculations happening where for the current price we are traversing in the reverse direction checking how many values are <= the current one but we can use an approach which takes advantage of previously calculated values to get the new answer

        # self.stack.append(price)
        # max_days = 0
        # curr_idx = len(self.stack) - 1
        # while curr_idx >= 0:
        #     if self.stack[curr_idx] <= price:
        #         max_days += 1
        #     else:
        #         break
        #     curr_idx -= 1
        
        # return max_days

        # optimal solution using a monotonically decreasing stack

        span = 1 # by default the span of a stock price is 1 so we start off with that
        # the idea is that when we encounter some price before the one to be added and that price is <= the current price we want to update our span by 1

        # however let's say there's some stock before the new one that already had a certain span, meaning that there were "span" elements less than or equal to itself so with the current stock if the previous stock was less than this and had a span, we need to include that previous stock's span along with this one which essentially helps us avoid the recalculation
        # we use a monotonically decreasing stack here so that it's easy to detect when we've found a stock price that doesn't follow the default ordering
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        
        self.stack.append([price, span]) # we store each stock as a pair with its price and span otherwise we would need 2 stacks which is quite cumbersome to manage

        return span
    
obj = StockSpanner()
prices = [100, 80, 60, 70, 60, 75, 85]
for price in prices:
    days = obj.next(price)
    print(days)