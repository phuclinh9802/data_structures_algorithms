# Linked list: a data structure that is linked through nodes
# to create a linked list, first create a node class, then linked list class with head node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        # create a new node
        node = Node(data)
        # set next node of current node to current head
        node.next = self.head
        # assign head to point to current node to insert to the beginning of the linked list
        self.head = node

    def addEnd(self, data):
        # create new node
        node = Node(data)
        if self.head is None:
            node.next = self.head
            self.head = node

        else:
            curNode = self.head
            while curNode.next:
                curNode = curNode.next
            node.next = curNode.next
            curNode.next = node

    def insert(self, data, index):
        node = Node(data)
        prevNode = self.head
        curNode = self.head

        if index == 0:
            self.head = node
            node.next = curNode
            return

        for i in range(index):
            curNode = curNode.next

        if curNode.next is not None or (not curNode.next and curNode is not None):
            node.next = curNode
            prevNode.next = node

        elif not curNode.next and not curNode:
            print("Error!")

    # remove data at first occurence
    def remove(self, data):
        node = self.head
        prevNode = self.head

        if node.next is None:
            self.head = None
            return

        if node.data == data:
            self.head = node.next
            return

        while node:
            if node.data == data:
                prevNode.next = node.next
                return
            prevNode = node
            node = node.next

        return False

    def traverse(self):
        # we need to traverse through the singly linked list
        node = self.head

        while node:
            print(node.data, '->', end=" ")
            node = node.next

        print(None)


linked_list = LinkedList()
linked_list.add(6)
linked_list.insert(4, 0)
linked_list.insert(10, 1)
linked_list.addEnd(1248)
linked_list.traverse()
# linked_list.remove(6)
linked_list.remove(4)

linked_list.traverse()



