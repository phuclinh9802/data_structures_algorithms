# Ford-Fulkerson
# Definition: a greedy algorithm that finds the longest path/flow in a graph/network

# Algorithm
# 1. Initialize all flows to 0
# 2. while the current solution is feasible, push it to the current solution set
# - For this algorithm, while there is an augmenting path between source and sink, add this path to the flow
# If not, the item is rejected and never reconsidered.
# 3. Update the residual graph

# Terms
# Augmenting Path: path available in the graph
# Residual graph: flow network with additional flow
# Residual Capacity: capacity of the edge after subtracting the flow from the maximum capacity

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    # BFS as search algorithm
    def bfs(self, s, t, parent):
        visited = [False] * (self.ROW)
        queue = []

        queue.append(s)
        visited[s] = True # root is always true when visited

        while queue:
            current = queue.pop(0)

            for i, val in enumerate(self.graph[current]):
                if visited[i] == False and val > 0:
                    queue.append(i)
                    visited[i] = True
                    parent[i] = current

        return True if visited[t] else False

    # ford-fulkerson algorithm
    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0

        while self.bfs(source, sink, parent):
            print(self.bfs(source, sink, parent))
            print('source:',source,'sink:', sink)
            path_flow = float('Inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                print('path_flow:',path_flow)
                s = parent[s]

            # Adding the path flows
            max_flow += path_flow
            print('max_flow:',max_flow)

            # Update the residual values of edges
            v = sink
            print('v:',v)
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

            print(self.graph)
        return max_flow

graph = [[0, 8, 0, 0, 3, 0],
         [0, 0, 9, 0, 0, 0],
         [0, 0, 0, 0, 7, 2],
         [0, 0, 0, 0, 0, 5],
         [0, 0, 7, 4, 0, 0],
         [0, 0, 0, 0, 0, 0]]

g = Graph(graph)

source = 0
sink = 5

print("Max Flow: %d " % g.ford_fulkerson(source, sink))