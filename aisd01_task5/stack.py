class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() < 1:
            return None
        return self.stack.pop()

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if self.size() < 1:
            return None
        return self.stack[-1]