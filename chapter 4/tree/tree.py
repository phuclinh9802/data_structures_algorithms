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

    # Full Binary Tree: a node that has 0 or 2 children
    def isFullBinaryTree(self, root):
        if root is None:
            return True

        if root.left is None and root.right is None:
            return True

        if root.left is not None and root.right is not None:
            return self.isFullBinaryTree(root.left) and self.isFullBinaryTree(root.right)

        return False

    def depth(self, root):
        d = 0
        while root:
            d += 1
            root = root.left
        return d

    # A Perfect Binary Tree: a tree that has both left and right children from every node from every level, and leaf nodes should be in the same level.
    # depth: O(ln(n)) where n is # of nodes
    # # of nodes: = 2^(h+1) - 1
    # leaf nodes: 2^h
    def isPerfectBinaryTree(self, root, d, level=0):
        # base case: if root is null
        if root is None:
            return True

        print('d: ', d)


        if root.left is None and root.right is None:
            return (d == level + 1)

        # only 1 child is None
        if root.left is None or root.right is None:
            return False

        return self.isPerfectBinaryTree(root.left, d, level + 1) and self.isPerfectBinaryTree(root.right, d, level + 1)

    # count # of nodes
    def countNodes(self, root):
        if root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    # Complete Binary Tree: all nodes leaning towards the left
    def isCompleteBinaryTree(self, root, index, num_nodes):
        if root is None:
            return True

        if index >= num_nodes:
            return False

        return self.isCompleteBinaryTree(root.left, 2 * index + 1, num_nodes) and self.isCompleteBinaryTree(root.right, 2 * index + 2, num_nodes)

    def isBalancedBinaryTree(self, root, height):
        if root is None:
            return True

        left_height = Height()
        right_height = Height()

        l = self.isBalancedBinaryTree(root.left, left_height)
        r = self.isBalancedBinaryTree(root.right, right_height)

        # update current root node's height
        height.height = max(left_height.height, right_height.height) + 1

        if abs(left_height.height - right_height.height) <= 1:
            return l and r

        return False



class Height:
    def __init__(self):
        self.height = 0



# tree = Node(10)
# tree.insert(3)
# tree.insert(4)
# tree.insert(12)
# tree.insert(13)
# tree.print()
# print(tree.inorder(tree))
# print(tree.preorder(tree))
# print(tree.postorder(tree))
# print(tree.isFullBinaryTree(tree))

root = Node(2)
root.insert(1)
root.insert(3)
root.left.print()
root.right.print()
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)

if root.isCompleteBinaryTree(root, 0, root.countNodes(root)):
    print('The tree is a complete binary tree')

if (root.isPerfectBinaryTree(root, root.depth(root))):
    print("The tree is a perfect binary tree")
else:
    print("The tree is not a perfect binary tree")

height = Height()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)

if root.isBalancedBinaryTree(root, height):
    print('The tree is balanced')
else:
    print('The tree is not balanced')