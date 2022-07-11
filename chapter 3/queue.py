# queue: FIFO
# operations: enqueue, dequeue, peek, isEmpty
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, data):
        # init
        node = Node(data)
        # check if last is null
        if self.last is not None:
            self.last.next = node
        self.last = node

        # check if first is null
        if self.first is None:
            self.first = self.last

    def dequeue(self):
        # check if queue is empty
        if self.first is None:
            return False

        data = self.first.data
        self.first = self.first.next

        if self.first is None:
            self.last = None
        return data

    def peek(self):
        return self.first.data

    def isEmpty(self):
        return True if self.first is None else False

    def print(self):
        node = self.first
        while node:
            print(node.data, '->', end=' ')
            node = node.next

        print(None)

queue = Queue()
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue.dequeue())
queue.print()