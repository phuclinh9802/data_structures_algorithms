import collections


def bt_level_order_traversal(root):
    # use bfs approach

    q = collections.deque([root])

    res = []

    while q:
        # get length of q which is # of node for current level
        qLen = len(q)
        level = []

        for _ in range(qLen):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)

        if level:
            res.append(level)

    return res

