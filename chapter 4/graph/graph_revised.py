# Graph: a collection of nodes and edges between them
# implementation: DFS & BFS
# DFS -> go from root to child to grandchild -> ... until reaching the end, then go to the next child of root
# BFS -> go from every child of parent, then every child of that child -> level to level

import collections

def dfs(graph, root, visited=None):
    # first, we check if visited is none, then we create a new visited set
    if visited is None:
        visited = set()
    visited.add(root)

    # go through root's child, then go recursively to root's child's child & so on
    for child in graph[root] - visited: # this is to get the value in graph[root] set but not in visited set
        dfs(graph, child, visited)

    return visited

def bfs(graph, root):
    # for bfs, we consider queue and visited set
    visited, queue = set(), collections.deque([root])
    visited.add(root)

    # while loop to check if queue is null, if not, we store the dequeued node, then we go through every neighbor of that node
    # then check if each of them is inside visited node -> if not, then add them
    while queue:
        vertex = queue.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited

def route_between_routes(graph, start, end):
    visited = bfs(graph, start)
    return end in visited


graph = {
    '0': set(['1','2']),
    '1': set(['2']),
    '2': set(['1']),
    '3': set(['']),
    '4': set(['5']),
    '5': set(['4'])
}

print(dfs(graph, '4'))
print(bfs(graph, '0'))
print('--------')
print(route_between_routes(graph, '0', '2'))