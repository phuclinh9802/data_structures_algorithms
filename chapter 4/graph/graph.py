# Graph
# Data structure like a tree, but tree doesn't have cycles
# Use Adjacency List / Matrix to visualize

# class Graph:
#     def __init__(self, edge_list, num_nodes):
#         self.adjacency_list = [[] for _ in range(num_nodes)]
#
#         for (origin, dest) in edge_list:
#             self.adjacency_list[origin].append(dest)
#
# def print_graph(graph):
#     for origin in range(len(graph.adjacency_list)):
#         for dest in graph.adjacency_list[origin]:
#             print(origin, '->', dest, end=' ')
#
#         print()
#
#
# edge_list = [(0, 1), (1, 2), (2, 3), (0, 2), (3, 2), (4, 5), (5, 4)]
# num_of_nodes = 6
#
# graph = Graph(edge_list, num_of_nodes)
# print_graph(graph)

# algorithm:
# start from any node
# add to visited set
# then go through current node's neighbors by using for loop
# recursively do dfs with start node being first neighbor being visited
# etc

import collections

def dfs(graph, start, visited=None):
    # check if visited is null
    if visited is None:
        visited = set()

    # if not, then we add start node to visited
    visited.add(start)

    # go through for loop to go down the road
    for neighbor in graph[start] - visited:
        dfs(graph, neighbor, visited)

    return visited

def bfs(graph, start):
    # for bfs, we need a queue and a visited set
    visited, queue = set(), collections.deque([start])
    visited.add(start)

    while queue:
        # remove the current node and check for that node's neighbors
        vertex = queue.popleft()

        # go through each vertex's neighbor and check if it's inside visited set -> if not: add it to visited + enqueue
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited



graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

print(dfs(graph, '0'))
print(bfs(graph, '0'))











