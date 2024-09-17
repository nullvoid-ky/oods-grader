class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, key):
        # Step 1: Perform normal BST insert
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Step 2: Update height of this ancestor node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Step 3: Get the balance factor
        balance = self.getBalance(root)

        # Step 4: If the node becomes unbalanced, perform rotations
        if balance > 1 and key < root.left.key:  # Left Left Case
            print("Left Left Rotation")
            return self.rightRotate(root)
        if balance < -1 and key > root.right.key:  # Right Right Case
            print("Right Right Rotation")
            return self.leftRotate(root)
        if balance > 1 and key > root.left.key:  # Left Right Case
            print("Left Right Rotation")
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and key < root.right.key:  # Right Left Case
            print("Right Left Rotation")
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

        return y

    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def display(self, node, level=0):
        if node:
            self.display(node.right, level + 1)
            print('     ' * level, node.key)
            self.display(node.left, level + 1)

# Main driver function
if __name__ == "__main__":
    tree = AVLTree()
    root = None

    print("*** AVL Tree Insert Element ***")
    input_data = input("Enter Input: ")
    data = list(map(int, input_data.split()))

    for num in data:
        print(f"insert : {num}")
        root = tree.insert(root, num)
        tree.display(root)
        print("====================")
