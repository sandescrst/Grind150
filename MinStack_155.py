class MinStack:
    def __init__(self, val):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
    def pop(self):
        self.stack.pop()
        self.minStack.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.minStack[-1]

