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

    def removeDup(self):
        node = self.head
        if node is None or node.next is None:
            return

        # else
        # hash_map
        hash_map = {}
        prev_node = self.head
        while node:
            if node.data in hash_map:
                prev_node.next = node.next

            elif node.data not in hash_map:
                hash_map[node.data] = 1
                prev_node = node

            node = node.next

    def find_element(self, data):
        node = self.head
        if node is None or node.next is None:
            return node.data

        index = 0
        while node:
            if node.data == data:
                return index

            else:
                node = node.next
                index += 1

        return False

    def kth_to_last(self, k):
        # length - k
        length = self.get_length()
        print(length)
        true_length = length - k
        node = self.head
        # assuming return last el if k >= length
        i = 0
        while node and i < true_length:
            node = node.next
            i += 1

        return node.data


    def delete_mid(self, data):
        node = self.head
        # if data at head -> not removing
        if node.data == data:
            return

        # if data at end -> not removing
        while node:
            if node.data == data and node.next is None:
                return
            node = node.next

        # else, remove data in the middle
        self.remove(data)

    # (2 -> 6 -> 3) + (3 -> 5 -> 4) = 362 + 453 = 815 -> (5 -> 1 -> 8)
    def sum_list(self, list1, list2):
        # keep track of each list
        cur_list1 = list1.head # head of a linked list is a node
        cur_list2 = list2.head
        length = list1.get_length() - 1
        sum = 0
        i = 0

        while i <= length and cur_list1 and cur_list2:
            sum += (pow(10, i) * cur_list1.data) + (pow(10, i) * cur_list2.data)
            i += 1
            cur_list1 = cur_list1.next
            cur_list2 = cur_list2.next

        node = Node(sum % 10)
        curList = LinkedList()
        node.next = curList.head
        curList.head = node
        curNode = curList.head
        sum = int(sum / 10)
        while sum > 0:
            while curNode.next:
                curNode = curNode.next
            node = Node(sum % 10)
            node.next = curNode.next
            curNode.next = node
            sum = int(sum / 10)
            curNode = curList.head

        return curList


    def partition(self, data):
        return

    def get_length(self):
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next

        return length


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
linked_list.insert(10, 1)
linked_list.addEnd(1248)
linked_list.addEnd(1248)
linked_list.traverse()
linked_list.removeDup()
linked_list.traverse()
# print(linked_list.kth_to_last(4))
linked_list.delete_mid(1248)
linked_list.delete_mid(4)
# linked_list.delete_mid(10)
linked_list.traverse()

list = LinkedList()
list1 = LinkedList()
list1.add(3)
list1.add(9)
list1.add(3)
list2 = LinkedList()
list2.add(1)
list2.add(2)
list2.add(3)
list.sum_list(list1, list2).traverse()
