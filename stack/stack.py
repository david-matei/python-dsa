class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

    def is_empty(self):
        return not self.items

    def size(self):
        return len(self.items)


stack = Stack()

stack.push(5)
print(stack.items)
stack.push(6)
print(stack.items)
stack.push(7)
print(stack.items)

print(stack.peek())
stack.pop()
print(stack.peek())
print(stack.items)
print(stack.is_empty())
print(stack.size())
stack.pop()
stack.pop()
print(stack.is_empty())
print(stack.size())