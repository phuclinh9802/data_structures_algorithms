# Kruskal: An MST algorithm (greedy algorithm) that takes a graph as input and
# finds the subset of all edges of that graph which
# 1. can form a tree that includes every vertex (means that no cycles)
# 2. has the min sum of weight among the trees

class Graph:
    def __init__(self, vertices):
        self.graph = []
        self.vertices = vertices

    def add_edge(self, u, v, weight):
        self.graph.append([u, v, weight])

    # search
    def find(self, parent, i):
        if parent[i] == i:
            # print('parent[i]:', parent[i], 'i:', i)
            return i
        return self.find(parent, parent[i])

    # union find
    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        # print('xroot:', xroot)
        yroot = self.find(parent, y)
        # print('yroot:', yroot)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot

        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        else:
            parent[yroot] = xroot
            rank[xroot] += 1

        print('parent[xroot]:',parent[xroot])
        print('parent[yroot]:', parent[yroot])
        print('rank[xroot]:', rank[xroot])


    # kruskal's algorithm
    def kruskal(self):
        result = []
        i, e = 0, 0
        # sort by weight
        self.graph = sorted(self.graph, key=lambda item : item[2])
        print(self.graph)
        parent = []
        rank = []

        # loop through each vertex
        for node in range(self.vertices):
            # push node into parent list
            parent.append(node)
            # initialize every vertex's rank to 0
            rank.append(0)

        # loop through each edge
        while e < self.vertices - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            print('find x:', x)
            y = self.find(parent, v)
            print('find y:', y)
            if x != y:
                e += 1
                print('edge:', e)
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
            print('result:', result)
            print('-----')
        for u, v, weight in result:
            print("%d - %d: %d" % (u, v, weight))


g = Graph(6)
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 2)
g.add_edge(1, 0, 4)
g.add_edge(2, 0, 4)
g.add_edge(2, 1, 2)
g.add_edge(2, 3, 3)
g.add_edge(2, 5, 2)
g.add_edge(2, 4, 4)
g.add_edge(3, 2, 3)
g.add_edge(3, 4, 3)
g.add_edge(4, 2, 4)
g.add_edge(4, 3, 3)
g.add_edge(5, 2, 2)
g.add_edge(5, 4, 3)
g.kruskal()
