# Heap: special data structure
# Min-heap: parent <= children
#  - Swap when parent node > left child or right child
#  - swap smaller child with parent
# Max-heap: parent >= children
import sys


class MinHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize # size of heap
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = -1

    # return position (index) of parent of that node
    def parent(self, pos):
        return pos // 2

    # return position (index) of left child
    def left_child(self, pos):
        return pos * 2

    # return position (index) of right child
    def right_child(self, pos):
        return pos * 2 + 1

    # inserting
    def insert(self, data):
        # check if current size exceeds maxsize
        if self.size > self.maxsize:
            return

        # else
        # keep track of current node
        # increase size
        self.size += 1
        self.Heap[self.size] = data

        current = self.size

        # condition to move bottom-up
        # if current node < its parent -> move up
        while self.Heap[self.size] < self.Heap[self.parent(self.size)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def print(self):
        for i in range(1, (self.size // 2) + 1):
            print('parent: ', self.Heap[i])
            print('left: ', self.Heap[i*2])
            print('right: ', self.Heap[i * 2 + 1])



    # check if leaf node
    def isLeaf(self, pos):
        return pos * 2 > self.size

    # swap
    def swap(self, i, j):
        self.Heap[i], self.Heap[j] = self.Heap[j], self.Heap[i]

    # heapify node at position
    def heapify(self, i):
        if self.isLeaf(i):
            # check if parent > left or parent > right
            if self.Heap[i] > self.Heap[self.left_child(i)] or self.Heap[i] > self.Heap[self.right_child(i)]:
                if self.Heap[self.left_child(i)] > self.Heap[self.right_child(i)]:
                    self.swap(i, self.left_child(i))
                    self.heapify(self.left_child(i))

                else:
                    self.swap(i, self.right_child(i))
                    self.heapify(self.right_child(i))

    def min_heap(self):
        for i in range((self.size // 2), 0, -1):
            self.heapify(i)



heap = MinHeap(10)
heap.insert(3)
heap.insert(9)
heap.insert(4)
heap.insert(19)
heap.insert(20)
heap.insert(1)
heap.min_heap()
# heap.heapify(3)
# print(heap.Heap)
heap.print()