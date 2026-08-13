class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_last(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return

        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def add_first(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return

        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def remove_first(self):
        if self.head is None:
            return

        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1

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
        self.size -= 1

    def get_at_index(self, index):
        curr = self.head
        i = 0
        while curr is not None:
            if i == index:
                return curr.val
            curr = curr.next
            i+=1
        return "Invalid input"

    def insert_at_index(self, index, value):
        if index < 0 or index > self.size:
            return

        new_node = Node(value)

        # if index == 0:
        #     self.add_first(value)

        if index == 0:
            new_node.next = self.head
            self.head = new_node

            if self.tail is None:
                self.tail = new_node

            self.size += 1
            return

        curr = self.head
        i = 0
        while curr is not None:
            if i == index - 1:
                next_node = curr.next
                curr.next = new_node
                new_node.next = next_node
                if curr == self.tail:
                    self.tail = new_node
                self.size += 1
                return

            curr = curr.next
            i += 1

    def remove_at_index(self, index):
        if index < 0 or index >= self.size:
            return

        if self.head is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.size -= 1
            return

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        curr = self.head
        i = 0

        while curr:
            if i == index - 1:
                if curr.next == self.tail:
                    self.tail = curr
                curr.next = curr.next.next
                self.size -= 1
                return
            i += 1
            curr = curr.next

    def reverse(self):
        old_head = self.head

        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev
        self.tail = old_head