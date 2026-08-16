class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_first(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.size += 1
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.size += 1

    def add_last(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.size += 1
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.size += 1

    def remove_first(self):
        if self.head is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.size -= 1
            return

        self.head = self.head.next
        self.head.prev = None
        self.size -= 1

    def remove_last(self):
        if self.head is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.size -= 1
            return

        self.tail.prev.next = None
        self.tail = self.tail.prev
        self.size -= 1

    def get_at_index(self, index):
        if index < 0 or index >= self.size:
            return None

        curr = self.head
        i = 0

        while curr:
            if index == i:
                return curr.val
            curr = curr.next
            i += 1

        return None

    def insert_at_index(self, val, index):
        new_node = Node(val)

        if index < 0 or index > self.size:
            return

        if index == 0:
            if self.size == 0:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node

            self.size += 1
            return

        if index == self.size:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.size += 1
            return

        curr = self.head
        i = 0

        while curr is not None:
            if index - 1 == i:
                next_node = curr.next

                curr.next = new_node
                new_node.prev = curr

                new_node.next = next_node
                next_node.prev = new_node

                self.size += 1
                return

            i += 1
            curr = curr.next

    def remove_at_index(self, index):
        if index < 0 or index >= self.size:
            return

        if index == 0:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None

            self.size -= 1
            return

        curr = self.head
        i = 0

        while curr:
            if index - 1 == i:
                if curr.next == self.tail:
                    self.tail = curr
                    curr.next = None
                else:
                    curr.next = curr.next.next
                    curr.next.prev = curr
                self.size -= 1
                return
            curr = curr.next
            i += 1

