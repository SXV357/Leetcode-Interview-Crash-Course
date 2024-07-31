# 232

class MyQueue:
    """
    Simulating a queue using 2 stacks
    """
    def __init__(self):
        self.first = [] # keeps track of very first element added to the queue
        self.remaining = [] # keeps track of every other element apart from the very first element
        self.queue = [] # the actual queue that is formed by combining both the above stacks

    def push(self, x: int) -> None:
        """
        O(n) amortized(we could be combining an empty stack with a non-empty 1 element stack or how many ever so it averages out)
        """
        # if we are adding something to the queue for the very first time we add it to the first stack
        if not self.first:
            self.first.append(x)
        # in all the other cases, we add the element to the remaining stack
        else:
            self.remaining.append(x)
        self.queue = self.first + self.remaining # update the queue after this change

    def pop(self) -> int:
        """
        O(n) amortized since the list slicing could involve either 1 element only or multiple elements and it averages out
        """
        # equivalent of deque's popleft(). since we're maintaining the first element added to the queue in the first stack we can get that element easily  
        res = self.first.pop()
        # now the first stack needs to be updated so we add the first element from the remaining stack and update the remaining stack as well
        if self.remaining:
            self.first.append(self.remaining[0])
            self.remaining = self.remaining[1:]
        self.queue = self.first + self.remaining # update the queue
        return res

    def peek(self) -> int:
        """
        O(1) TC
        """
        # if we peek in a scenario where nothing's left in the remaining stack
        if self.first:
            return self.first[0]
        return self.remaining[0]

    def empty(self) -> bool:
        """
        O(1) TC
        """
        return not self.queue

obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
print(obj.pop())
obj.push(5)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()