
class Solution:
    def kth_smallest_el_in_BST(self, root, k):
        # we can approach in 2 ways, recursively and iteratively, with the same result
        # 1. Recursive
        self.newK = k
        self.res = float("inf")

        def check_kth(root):
            if root is None:
                return

            # inorder traversal
            check_kth(root.left)
            self.newK -= 1

            if self.newK == 0:
                self.res = min(self.res, root.val)
                return
            check_kth(root.right)

        check_kth(root)

        return self.res

    def kth_smallest_el_in_BST_iterative(self, root, k):
        # 2. Iterative
        n = 0
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            n += 1

            if n == k:
                return current.val

            current = current.right




