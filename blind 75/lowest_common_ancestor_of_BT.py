def lowest_ancestor(root, p, q):
    # check if root > p and q -> left, root < p and q -> right, else return root
    while root:
        if p.val < root.val > q.val:
            root = root.left
        elif p.val > root.val < q.val:
            root = root.right
        else:
            return root

    return
