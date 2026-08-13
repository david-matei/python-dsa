class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_last(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def add_first(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def remove_first(self):
        if self.head is None:
            return
        self.head = self.head.next
        if self.head is None:
            self.tail = None

    def remove_last(self):
        if self.head is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        curr = self.head
        while curr.next.next is not None:
            curr = curr.next

        curr.next = None
        self.tail = curr
