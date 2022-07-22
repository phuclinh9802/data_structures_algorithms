# Prim: same as Kruskal: MST algorithm that takes a graph as input and finds the subset of the edges
# of that graph which
# 1. Form a tree that includes every vertex
# 2. has a min sum of weights among all the trees

# Algorithm:
# 1. Initialize the MST with a vertex chosen at random
# 2. Find all the edges that connect the tree to new vertices, find the nmin and add it to the tree
# 3. Keep repeating step 2 until we get an MST.

INF = 10000
# vertices
vertices = 5
# we create a 2d array vertices x vertices
# as adjacency matrix
G = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]

# we create an array to track selected vertex
# selected will become true -> 1, else 0 -> False
selected = [0 for i in range(vertices)]
# set number of edge in the MST to 0
no_edge = 0

# choose 1st vertex at index 0 to True -> selected
selected[0] = True

# then create a while loop to loop through edges from no_edge -> V - 2
# edges are always less than # of vertices by 1
while no_edge < vertices - 1:
    # for every vertex, find adjacent vertices & calculate the distance
    # from the vertex selected at step 1
    # if vertex is already in the set S, discard
    # else choose another vertex nearest to selected vertex
    # at step 1
    min = INF
    x = 0
    y = 0

    print('Edge : Weight')
    # loop through vertices
    for i in range(vertices):
        if selected[i]:
            for j in range(vertices):
                # if not visited yet and there is a connection
                # between i and j vertices
                if (not selected[j]) and G[i][j]:
                    if min > G[i][j]:
                        # update min weight
                        min = G[i][j]
                        # update to next connection
                        x = i
                        y = j
    print(str(x) + '-' + str(y) + ':' + str(G[x][y]))
    selected[y] = True
    no_edge += 1



