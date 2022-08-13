def flip_bt_to_match_preorder(root, voyage):
    # we use preorder traversal
    # 1. check if current node's value matches current voyage's el. If not, return [-1]
    # 2. if so, increment i by 1, then continue checking left child if it matches current voyage[i]
    #    if not, flip the children, and add current parent's val to result
    # 3. then we continue the traversal by appending right child then left child (if either of them is not null)

    flips = []
    i = 0
    nodes = [root]
    while nodes:
        # save & remove current parent node
        parent = nodes.pop()

        # check if parent node's val matches voyage[i]
        if parent.val != voyage[i]:
            return [-1]

        # else, check parent's left child
        i += 1

        if parent.left and parent.left.val != voyage[i]:
            # swap left and right child
            parent.left, parent.right = parent.right, parent.left
            flips.append(parent.val)

        # continue traversing, make sure to add right node first then left, since we pop() the stack
        if parent.right:
            nodes.append(parent.right)
        if parent.left:
            nodes.append(parent.left)

    return flips



