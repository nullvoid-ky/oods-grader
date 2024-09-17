class AVLTree:
    class AVLNode:
        def __init__(self, data, left=None, right=None):
            self.data = int(data)
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.height = self.setHeight()

        def __str__(self):
            return str(self.data)

        def setHeight(self):
            a = self.getHeight(self.left)
            b = self.getHeight(self.right)
            self.height = 1 + max(a, b)
            return self.height

        def getHeight(self, node):
            return -1 if node is None else node.height

        def balanceValue(self):
            return self.getHeight(self.right) - self.getHeight(self.left)

    def __init__(self, root=None):
        self.root = None if root is None else root

    def add(self, data):
        self.root = AVLTree._add(self.root, data)

    @staticmethod
    def _add(root, data):
        if root is None:
            return AVLTree.AVLNode(data)

        if int(data) < root.data:
            root.left = AVLTree._add(root.left, data)
        else:
            root.right = AVLTree._add(root.right, data)

        root.setHeight()
        balance = root.balanceValue()

        # Check for imbalance and rotate accordingly
        if balance < -1:
            if root.left and int(data) < root.left.data:
                root = AVLTree.rotateRightChild(root)  # Left-Left case
            else:
                root.left = AVLTree.rotateLeftChild(root.left)  # Left-Right case
                root = AVLTree.rotateRightChild(root)
        elif balance > 1:
            if root.right and int(data) > root.right.data:
                root = AVLTree.rotateLeftChild(root)  # Right-Right case
            else:
                if root.right:
                    root.right = AVLTree.rotateRightChild(root.right)  # Right-Left case
                root = AVLTree.rotateLeftChild(root)

        return root

    def rotateLeftChild(root):
        if root is None or root.right is None:
            return root
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        root.setHeight()
        new_root.setHeight()
        return new_root

    def rotateRightChild(root):
        if root is None or root.left is None:
            return root
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        root.setHeight()
        new_root.setHeight()
        return new_root

    def postOrder(self):
        print("AVLTree post-order : ", end="")
        self._postOrder(self.root)
        print()

    def _postOrder(node):
        if node is not None:
            AVLTree._postOrder(node.left)
            AVLTree._postOrder(node.right)
            print(node.data, end=" ")

    def printTree(self):
        AVLTree._printTree(self.root)
        print()

    def _printTree(node, level=0):
        if node is not None:
            AVLTree._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            AVLTree._printTree(node.left, level + 1)

avl1 = AVLTree()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AD":
        avl1.add(i[3:])
    elif i[:2] == "PR":
        avl1.printTree()
    elif i[:2] == "PO":
        avl1.postOrder()


