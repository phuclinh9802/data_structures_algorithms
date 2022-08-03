def clone_graph(node):
    # this uses dfs and a hash_map to store visited edge
    hash_map = {}

    # nested dfs function
    def dfs(node):
        # base case: if node is in hash_map -> return that value
        if node in hash_map:
            return hash_map[node]

        # else
        # create a copy, then set that copy as a value of current node
        copy = Node(node.val)
        hash_map[node] = copy

        # loop through each neighbor and append using dfs
        for neighbor in node.neighbors:
            copy.neighbors.append(dfs(neighbor))

        return copy

    return dfs(node) if node else None