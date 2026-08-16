class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self._size = 0

    #push
    def push(self, val):
        #create new node
        new_node = Node(val)
        #make the new node the head
        #the head is where we pop from, the top of the stack
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    #pop
    def pop(self):
        if not self.head:
            return None
        head = self.head
        self.head = self.head.next
        self._size -= 1
        return head.val

    #peek
    def peek(self):
        if not self.head:
            return None
        return self.head.val

    #is_empty
    def is_empty(self):
        return self.head is None

    #size
    def size(self):
        return self._size

    def clear(self):
        self.head = None
        self._size = 0

    def contains(self, val):
        curr = self.head
        while curr:
            if curr.val == val:
                return True
            curr = curr.next

        return False

stack = Stack()