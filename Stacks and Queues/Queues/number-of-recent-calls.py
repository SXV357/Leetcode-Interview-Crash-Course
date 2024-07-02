# 933

from collections import deque
class RecentCounter:
    def __init__(self):
        # initialize a queue to store the requests along with number of requests but the second initialization is not needed since the length of the queue represents the number of valid requests made
        self.requests = deque([])
        self.num_requests = 0

    def ping(self, t: int) -> int:
        """
        Time complexity: O(1) because all the arithmetic and queue operations take place in O(1) and the while loop also may or may not iterate for all values of `t`. One improvement is that we don't need to maintain `num_requests` due to the fact that after deleting all the out of bounds elements the length of the queue is the answer we can return
        Space complexity: O(`n`) where `n` is the number of calls made to this function. In the case where in every single call made to ping, the values fall within the range then no elements are ever popped off the queue and the queue keeps growing in size
        """
        # the latest request is always guaranteed to be valid so we add it to the queue and update number of requests
        self.requests.append(t)
        self.num_requests += 1

        # some older requests may not fit the constraints so we need to delete all of them until we have a queue where all requests were made in the last 3000ms
        while not t - 3000 <= self.requests[0] <= t:
            self.requests.popleft() # O(1) since we're using deque
            self.num_requests -= 1

        return self.num_requests

call = RecentCounter()

call.ping(1)
print(f"Requests: {call.requests}")
print(f"Num requests: {call.num_requests}")

call.ping(100)
print(f"Requests: {call.requests}")
print(f"Num requests: {call.num_requests}")

call.ping(3001)
print(f"Requests: {call.requests}")
print(f"Num requests: {call.num_requests}")

call.ping(3002)
print(f"Requests: {call.requests}")
print(f"Num requests: {call.num_requests}")