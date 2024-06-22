# simple implementation of a stack and the three major operations
    # push
    # pop
    # peek

class Stack():
    def __init__(self):
        self.stack = []
        self.length = 0
    
    def push(self, val: int) -> None:
        """
        Adds an element to the stack(in this case to the end of the array)
        """
        self.stack.append(val)
        self.length += 1

    def pop(self):
        """
        Removes the last added element and returns it
        """
        if not self.stack:
            return "Stack is empty"

        last = self.stack[self.length - 1]
        self.stack = self.stack[:self.length - 1]
        self.length -= 1
        return last

    def peek(self):
        """
        Returns the last added element
        """
        if not self.stack:
            return "Stack is empty"
        
        return self.stack[self.length - 1]

stack = Stack()

stack.push(10)
print(stack.stack)

stack.push(7)
print(stack.stack)

stack.push(15)
print(stack.stack)

print(stack.peek())

elem = stack.pop()
print(elem)
print(stack.stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())