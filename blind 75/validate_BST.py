def validate_BST(root):
    # recursion approach with nested function
    def check_BST(root, l, r): # we have 2 pointers inside params to update min and max
        if root:
            # check if current value of root is between 2 pointers
            if l < root.val < r:
                if check_BST(root.left, l, root.val) and check_BST(root.right, root.val, r):
                    return True
            return False

        return False

    return check_BST(root, -float("inf"), float("inf"))
