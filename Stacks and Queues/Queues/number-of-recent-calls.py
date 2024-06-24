# 933

from collections import deque

class RecentCounter:
    def __init__(self):
        # initialize a queue to store the requests along with number of requests but the second initialization is not needed since the length of the queue represents the number of valid requests made
        self.requests = deque([])
        self.num_requests = 0

    def ping(self, t: int) -> int:
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