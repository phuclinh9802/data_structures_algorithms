# AVL Tree
# Operations: Insert, Delete, LeftRotate, RightRotate, getHeight, getBalance
import sys


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left, self.right = None, None
        self.height = 1


class AVLTree:
    def insert(self, root, key):
        # Need to find the location from top-bottom first
        if not root:
            return TreeNode(key)

        elif key < root.key:
            root.left = self.insert(root.left, key)

        else:
            root.right = self.insert(root.right, key)

        # then, we get the height of current node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # get the balance factor
        balance_factor = self.getBalance(root)

        # check balance factor > 1 or < -1, then do the rotation accordingly
        if balance_factor > 1:
            if key < root.left.key: # right rotate
                return self.rightRotate(root)
            else: # left right rotate
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        elif balance_factor < -1:
            if key > root.right.key: # left rotate on right branch
                return self.leftRotate(root)
            else: # right left rotate
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    def delete(self, root, key):
        # find the node first
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else: # key = root.key
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right, temp.key)

        if root is None:
            return root

        # update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance_factor = self.getBalance(root)

        # balance the tree
        if balance_factor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root)
                return self.rightRotate(root)
        elif balance_factor < -1:
            if self.getBalance(root.right) <= 0:
                return self.rightRotate(root)
            else:
                root.right = self.rightRotate(root)
                return self.leftRotate(root)

        return root

    # left rotate with z being the root of the operation
    def leftRotate(self, x):
        y = x.right
        beta = y.left
        y.left = x
        x.right = beta
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y

    def rightRotate(self, y):
        x = y.left
        beta = x.right
        x.right = y
        y.left = beta

        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return x

    def print_avl(self, root):
        if root:
            print(root.key)
            self.print_avl(root.left)
            self.print_avl(root.right)

    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.key)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)


    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)


AVL = AVLTree()
root = None
nums = [33, 13, 52, 9, 21, 61, 8, 11]
for num in nums:
    root = AVL.insert(root, num)
AVL.print_avl(root)
AVL.printHelper(root, "", True)