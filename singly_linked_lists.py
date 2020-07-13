class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

# THIS HAS O(n) COMPLEXITY! NOONONONO!
# ll = Node(1)
# ll.next = Node(2)
# ll.next.next = Node(3)
# ll.next.next.next = Node(4)
# ll.next.next.next.next = Node(5)


class LinkedList:
    # Using this class and keeping track of tail, you get O(1)
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        newNode = Node(value)
        if self.is_empty():
            # no tail
            self.tail = newNode
            self.head = newNode
        else:
            self.tail.set_next(newNode)
            self.tail = newNode

    def is_empty(self):
        if self.tail is None and self.head is None:
            return True
        else:
            return False

    def pop(self):
        if self.is_empty():
            return
        else:
            # to get to the previous node, we must start at the beginning AND ITERATE
            i = self.head
            while i.get_next() is not self.tail:
                print(i)

            val = self.tail.get_value()
            self.tail = None
            # set self.tail to be previous node
            self.tail = i
            return val

    def remove_head(self):
        if self.is_empty():
            return
        elif self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val
        else:
            val = self.head.get_value()
            self.head = self.head.get_next()
            return val
