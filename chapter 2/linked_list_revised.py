# linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    # insert from beginning
    def insert(self, data):
        # create new node
        node = Node(data)
        # set next node to head
        node.next = self.head
        # set head to node
        self.head = node

    def insert_to_end(self, data):
        # set current to self.head
        current = self.head
        if current is None:
            self.head = Node(data)
            return


        while current.next:
            current = current.next
        node = Node(data)
        node.next = current.next
        current.next = node

    def remove(self, data):
        current = self.head
        prev = self.head
        if current.data == data:
            current = current.next
            self.head = current
            return

        while current:
            if current.data == data:
                current = current.next
                prev.next = current
                return
            prev = current
            current = current.next


        return -1

    def print(self):
        current = self.head

        while current:
            print(current.data, '->', end=' ')
            current = current.next
        print(None)

ll = LinkedList()
ll.insert_to_end(3)
ll.insert_to_end(4)
ll.insert_to_end(5)
ll.insert_to_end(6)
ll.insert_to_end(7)
ll.insert_to_end(8)
ll.insert_to_end(9)
ll.insert_to_end(10)
ll.print()
ll.remove(5)
ll.print()



