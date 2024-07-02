# 346

from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        # initialize max size, queue with the max size as well as current sum of all elements in the queue up to the maximum length
        self.size = size
        self.elems = deque([], self.size)
        self.curr_sum = 0

    def next(self, val: int) -> float:
        """
        Time complexity: O(1) because checking length of queue, updating current sum, indexing into queue, appending to queue and the average calculation arithmetic operation all take place in constant time
        Space complexity: O(`size`) because the queue can only store a max of `size` elements before the first one is popped off and the next element is added
        """
        # if the max length of a queue is reached and an element is added the first element is removed and the new element is appended to maintain the same length so to simulate that, we check whether we've already reached the max length and if so subtract the first element
        if len(self.elems) == self.size:
            self.curr_sum -= self.elems[0]
        
        # curr_sum holds the current sum of how many ever elements are in the queue so we update that including the queue and return the average
        self.curr_sum += val
        self.elems.append(val)
        return self.curr_sum / len(self.elems)

stream = MovingAverage(3)

print(stream.next(1))
print(stream.next(10))
print(stream.next(3))
print(stream.next(5))

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)