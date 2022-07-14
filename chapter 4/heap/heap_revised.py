# Heap - min heap
# Operations: parent, left, right, isLeaf, swap, insert, heapify, min_heap

class MinHeap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.Heap = [0] * (self.max_size + 1)
        self.Heap[0] = -1  * self.max_size
        self.FRONT = 1

    def parent(self, position):
        return position // 2

    def left_child(self, position):
        return position * 2

    def right_child(self, position):
        return (position * 2) + 1

    def isLeaf(self, position):
        return position * 2 > self.size

    def swap(self, i, j):
        self.Heap[i], self.Heap[j] = self.Heap[j], self.Heap[i]

    def insert(self, element):
        # base case
        if self.size > self.max_size:
            return

        # increment size + store updated size
        self.size += 1
        self.Heap[self.size] = element
        current = self.size

        # loop to go bottom-up
        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def heapify(self, position):
        if self.isLeaf(position):
            # check if parent > left or parent > right child
            if self.Heap[position] > self.Heap[self.left_child(position)] or self.Heap[position] > self.Heap[self.right_child(position)]:
                if self.Heap[self.left_child(position)] < self.Heap[self.right_child(position)]:
                    self.swap(position, self.left_child(position))
                    self.heapify(self.left_child(position))
                elif self.Heap[self.left_child(position)] > self.Heap[self.right_child(position)]:
                    self.swap(position, self.right_chilr(position))
                    self.heapify(self.right_child(position))

    def min_heap(self):
        for i in range((self.size // 2),  0, -1):
            self.heapify(i)

    def print(self):
        for i in range(1, self.size // 2 + 1):
            print('parent: ', self.Heap[i])
            print('left: ', self.Heap[i*2])
            print('right: ', self.Heap[i*2+1])



heap = MinHeap(10)
heap.insert(3)
heap.insert(4)
heap.insert(5)
heap.insert(11)
heap.insert(2)
heap.insert(22)
heap.insert(29)
heap.insert(10)
heap.print()