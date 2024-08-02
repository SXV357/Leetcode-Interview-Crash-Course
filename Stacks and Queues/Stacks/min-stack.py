# 155

from collections import deque

class MinStack:

    def __init__(self):
        self.stack = []
        self.curr_min = None # to keep track of the current minimum value until the last added element in the stack

    def push(self, val: int) -> None:
        # O(1)
        if not self.stack:
            self.curr_min = val
        else:
            self.curr_min = min(self.curr_min, val)
        
        # stack will consist of pairs of (current value added, minimum value in the stack as of this value)
        self.stack.append((val, self.curr_min))

    def pop(self) -> None:
        # O(1)
        self.stack.pop()
        if not self.stack:
            self.curr_min = None
        # we need to update the new minimum which we can do so by accessing the element at the top of the stack because the new value will be based on that
        else:
            self.curr_min = self.stack[-1][1]

    def top(self) -> int:
        # O(1)
        return self.stack[-1][0]

    def getMin(self) -> int:
        # O(1)
        return self.stack[-1][1]

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()