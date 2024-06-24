from collections import deque

# initialize a queue with certain elements
queue = deque([1, 2, 3, 4, 5])

# adding to the queue from the end
queue.append(6) # O(1)
print(f"Queue after appending 6: {queue}")

# adding to the queue from the start
queue.appendleft(0.5) # O(1) because we're using deque otherwise O(n) for a standard array
print(f"Queue after prepending 0.5: {queue}")

# deleting an item from the queue from the end
queue.pop() # O(1)
print(f"Queue after deleting 6: {queue}")

# deleting an element from the start of the queue
queue.popleft() # O(1) because we're using deque otherwise O(n) for a standard array
print(f"Queue after deleting 0.5: {queue}")

print(queue[0])