# Heap - MinHeap
# operations: parent, left_child, right_child, isLeaf, swap, insert, heapify, min_heap, print

import sys

class MinHeap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.Heap = [0] * (max_size + 1)
        self.Heap[0] = -1 * sys.maxsize

    def parent(self, pos):
        return pos // 2

    def left_child(self, pos):
        return pos * 2

    def right_child(self, pos):
        return pos * 2 + 1

    def isLeaf(self, pos):
        return pos * 2 > self.size

    def swap(self, i, j):
        self.Heap[i], self.Heap[j] = self.Heap[j], self.Heap[i]

    # remember: insert has base case to return if current size exceeds maxsize
    # then, we store the current node = key
    # then, we can check if that node is less than parent -> swap current node with its parent
    # then, move up current node by assigning current position to its parent's position
    def insert(self, key):
        if self.size > self.max_size:
            return

        self.size += 1
        self.Heap[self.size] = key
        current = self.size

        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def heapify(self, pos):
        if self.isLeaf(pos):
            if self.Heap[pos] > self.Heap[self.left_child(pos)] or self.Heap[pos] > self.Heap[self.Heap[self.right_child(pos)]]:
                if self.Heap[pos] > self.Heap[self.left_child(pos)]:
                    self.swap(pos, self.left_child(pos))
                    self.heapify(self.left_child(pos))
                else:
                    self.swap(pos, self.right_child(pos))
                    self.heapify(self.right_child(pos))

    def min_heap(self):
        for i in range(self.size // 2, 0, -1):
            self.heapify(i)

    def print(self):
        for i in range(1, (self.size // 2) + 1):
            print('parent:', self.Heap[i])
            print('left child:', self.Heap[i*2])
            print('right child:', self.Heap[i*2+1])


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