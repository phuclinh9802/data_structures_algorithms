# Graph
# Data structure like a tree, but tree doesn't have cycles
# Use Adjacency List / Matrix to visualize

class Graph:
    def __init__(self, edge_list, num_nodes):
        self.adjacency_list = [[] for _ in range(num_nodes)]

        for (origin, dest) in edge_list:
            self.adjacency_list[origin].append(dest)

def print_graph(graph):
    for origin in range(len(graph.adjacency_list)):
        for dest in graph.adjacency_list[origin]:
            print(origin, '->', dest, end=' ')

        print()


edge_list = [(0, 1), (1, 2), (2, 3), (0, 2), (3, 2), (4, 5), (5, 4)]
num_of_nodes = 6

graph = Graph(edge_list, num_of_nodes)
print_graph(graph)