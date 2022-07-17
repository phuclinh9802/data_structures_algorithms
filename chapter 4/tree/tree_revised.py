class Node:
    def __init__(self, data):
        self.data = data
        self.left, self.right = None, None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data


class LLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = LLNode(data)
        node.next = self.head
        self.head = node

    def addToEnd(self, data):
        node = LLNode(data)
        current = self.head

        while current.next:
            current = current.next

        node.next = current
        current.next = node

    def print(self):
        node = self.head
        while node:
            print(node.data.data, "->", end=" ")
            node = node.next

def createLL(root, lists, level):
    if root is None:
        return root

    if len(lists) == level: # current level to be considered is not in the list yet
        # create new linked list then append to the list
        linked_list = LinkedList()
        lists.append(linked_list)
    else:
        # assign linked_list to linked_list at current level of the list
        linked_list = lists[level]

    # recursion to add node in each level in a linked list
    linked_list.add(root)
    createLL(root.left, lists, level + 1)
    createLL(root.right, lists, level + 1)

def list_of_nodes(root):
    lists = []

    createLL(root, lists, 0)

    return lists

root = Node(10)
root.insert(3)
root.insert(16)
root.insert(4)
root.insert(19)
root.insert(5)
root.insert(20)

lists = list_of_nodes(root)

for list in lists:
    list.print()

print(None)
