class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
        def __init__(self):
            self.head = None
            self.tail = None
            self._size = 0

        def enqueue(self, val):
            new_node = Node(val)
            if self.head is None:
                self.head = self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node

            self._size += 1

        def dequeue(self):
            if self.head is None:
                return None

            node = self.head

            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next

            self._size -= 1
            node.next = None
            return node.val

        def size(self):
            return self._size

        def peek(self):
            if self._size == 0:
                return None
            return self.head.val

        def is_empty(self):
            return self._size == 0

        def clear(self):
            self.head = self.tail = None
            self._size = 0

        def __len__(self):
            return self._size

        def contains(self, val):
            curr = self.head

            while curr:
                if curr.val == val:
                    return True
                curr = curr.next

            return False

        def __str__(self):
            curr = self.head
            res = []
            while curr:
                res.append(curr.val)
                curr = curr.next

            queue_str = "->".join(str(x) for x in res)
            return queue_str