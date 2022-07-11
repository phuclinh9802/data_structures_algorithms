# Stack - Linked List approach

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.stack = []

    def add(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self.stack.append(self.top.data)

    def peek(self):
        return self.top.data

    def min_stack(self):
        return min(self.stack)

    def pop(self):
        data = self.top.data
        self.top = self.top.next
        self.stack.pop()
        return data

    def isEmpty(self):
        return True if self.top is None else False

    def get_length(self):
        count = 0

        node = self.top

        while node:
            count += 1
            node = node.next

        return count

    def traverse(self):
        node = self.top

        print(None, end=' ')
        while node:
            print('<-', node.data, end=' ')
            node = node.next

        print(end=' ')

stack = Stack()
stack.add(3)
stack.add(4)
stack.add(5)
# stack.traverse()
# print(stack.pop())
# stack.traverse()
#
# print(stack.min_stack())



class SetOfStack:
    def __init__(self):
        self.top = None

    def push(self, stack):
        # create new stack element
        node = Node(stack)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            return False

        _stack = self.top.data
        self.top = self.top.next

        return _stack

    def popAt(self, index):
        node = self.top
        prevNode = self.top
        # print('length', node.data.traverse())
        if index == 0:
            return self.pop()

        while index >= 1 and index < node.data.get_length():
            prevNode = node
            node = node.next
            index -= 1

        prevNode.next = node.next

    def print(self):
        stack = self.top
        while stack:
            print('|', end=' ')
            stack.data.traverse()
            print('|', end=' ')
            stack = stack.next
        print()


stack_2 = Stack()
stack_2.add(7)
stack_2.add(8)
stack_2.add(9)

stack_3 = Stack()
stack_3.add(10)
stack_3.add(11)
stack_3.add(12)


set_stack = SetOfStack()
set_stack.push(stack)
set_stack.push(stack_2)
set_stack.push(stack_3)
set_stack.print()
set_stack.popAt(0)
set_stack.print()