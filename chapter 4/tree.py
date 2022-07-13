# Binary Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        # check if tree is null
        if self.data:
            # check 2 conditions: self.data > data or < data
            if self.data > data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)

            elif self.data < data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

        else:
            self.data = data


    def print(self):
        if self.left:
            self.left.print()
        print(self.data)
        if self.right:
            self.right.print()

    # inorder
    def inorder(self, root):
        res = []
        if root:
            res = self.inorder(root.left)
            res.append(root.data)
            res += self.inorder(root.right)

        return res

    # preorder
    def preorder(self, root):
        res = []
        if root:
            res.append(root.data)
            res += self.preorder(root.left)
            res += self.preorder(root.right)

        return res

    # postorder
    def postorder(self, root):
        res = []
        if root:
            res = self.postorder(root.left)
            res += self.postorder(root.right)
            res.append(root.data)


        return res



tree = Node(10)
tree.insert(3)
tree.insert(4)
tree.insert(12)
tree.insert(13)
tree.print()
print(tree.inorder(tree))
print(tree.preorder(tree))
print(tree.postorder(tree))