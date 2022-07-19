# ford-fulkerson algorithm
# a greedy algorithm which finds the longest path in the graph
# algorithm:
# 1. Initialize all flows to 0
# 2. while augmenting path between source and sink is found -> add to the flow
# 3. update residual graph

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    # searching for each vertex with bfs - with parameters: source, sink, parent
    def bfs(self, s, t, parent):
        visited = [False] * self.ROW
        queue = [] # bfs needs to have a queue
        visited[0] = True
        queue.append(s)

        while queue:
            # dequeue and return that vertex
            current = queue.pop(0)

            for i, val in enumerate(self.graph[current]):
                if visited[i] == False and val > 0:
                    # add to queue
                    queue.append(i)
                    # set visited at i be true
                    visited[i] = True
                    # set parent of i = current
                    parent[i] = current

        return True if visited[t] else False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.ROW
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink

            # this is to find the min flow of an augmenting path
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink
            # this is to calculate the residual capacity
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

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