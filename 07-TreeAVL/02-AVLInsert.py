class TreeNode(object): 
    def __init__(self, val): 
        self.val = int(val)  # Ensure values are integers
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.val)

class AVL_Tree(object): 
    def insert(self, root, key):
        # Step 1: Perform the normal BST insertion
        if not root:
            return TreeNode(key)
        elif int(key) < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Step 2: Update the height of the ancestor node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Step 3: Get the balance factor to check whether this node became unbalanced
        balance = self.getBalance(root)

        # Step 4: If the node is unbalanced, perform the appropriate rotation
        # Left Left Case
        if balance > 1 and int(key) < root.left.val:
            print("Not Balance, Rebalance!")
            return self.rightRotate(root)

        # Right Right Case
        if balance < -1 and int(key) > root.right.val:
            print("Not Balance, Rebalance!")
            return self.leftRotate(root)

        # Left Right Case
        if balance > 1 and int(key) > root.left.val:
            print("Not Balance, Rebalance!")
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Right Left Case
        if balance < -1 and int(key) < root.right.val:
            print("Not Balance, Rebalance!")
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # Return the new root
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # Return the new root
        return y

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

def printTree90(node, level=0):
    if node:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

myTree = AVL_Tree() 
root = None

data = input("Enter Input : ").split()
for e in data:
    print("insert :", e)
    root = myTree.insert(root, e)
    printTree90(root)
    print("===============")
