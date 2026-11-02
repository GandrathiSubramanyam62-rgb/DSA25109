class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    def height(self, root):
        if root is None:
            return 0
        return root.height

    def balance(self, root):
        if root is None:
            return 0
        return self.height(root.left) - self.height(root.right)

    # Right Rotation (LL Case)
    def rightRotate(self, z):
        y = z.left
        T2 = y.right

        y.right = z
        z.left = T2

        z.height = 1 + max(self.height(z.left),
                           self.height(z.right))
        y.height = 1 + max(self.height(y.left),
                           self.height(y.right))

        return y

    # Left Rotation (RR Case)
    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left),
                           self.height(z.right))
        y.height = 1 + max(self.height(y.left),
                           self.height(y.right))

        return y

    # Insertion
    def insert(self, root, key):

        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)

        elif key > root.key:
            root.right = self.insert(root.right, key)

        else:
            return root

        root.height = 1 + max(self.height(root.left),
                              self.height(root.right))

        b = self.balance(root)

        # LL Case
        if b > 1 and key < root.left.key:
            return self.rightRotate(root)

        # RR Case
        if b < -1 and key > root.right.key:
            return self.leftRotate(root)

        # LR Case
        if b > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # RL Case
        if b < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    # Find Minimum Value
    def minValueNode(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    # Deletion
    def delete(self, root, key):

        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)

        elif key > root.key:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                return root.right

            elif root.right is None:
                return root.left

            temp = self.minValueNode(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.height(root.left),
                              self.height(root.right))

        b = self.balance(root)

        # LL Case
        if b > 1 and self.balance(root.left) >= 0:
            return self.rightRotate(root)

        # LR Case
        if b > 1 and self.balance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # RR Case
        if b < -1 and self.balance(root.right) <= 0:
            return self.leftRotate(root)

        # RL Case
        if b < -1 and self.balance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    # Searching
    def search(self, root, key):

        if root is None or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)

        return self.search(root.right, key)

    # Inorder Traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    # Preorder Traversal
    def preorder(self, root):
        if root:
            print(root.key, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # Postorder Traversal
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=" ")

    # Find Maximum Value
    def maxValueNode(self, root):
        current = root
        while current.right:
            current = current.right
        return current


# Main Program
tree = AVLTree()
root = None

while True:

    print("\n\n--- AVL TREE OPERATIONS ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Search")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Find Minimum")
    print("8. Find Maximum")
    print("9. Find Height")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter value: "))
        root = tree.insert(root, key)
        print("Inserted successfully")

    elif choice == 2:
        key = int(input("Enter value to delete: "))
        root = tree.delete(root, key)
        print("Deletion operation completed")

    elif choice == 3:
        key = int(input("Enter value to search: "))
        if tree.search(root, key):
            print("Element Found")
        else:
            print("Element Not Found")

    elif choice == 4:
        print("Inorder:", end=" ")
        tree.inorder(root)

    elif choice == 5:
        print("Preorder:", end=" ")
        tree.preorder(root)

    elif choice == 6:
        print("Postorder:", end=" ")
        tree.postorder(root)

    elif choice == 7:
        if root:
            print("Minimum:", tree.minValueNode(root).key)
        else:
            print("Tree is Empty")

    elif choice == 8:
        if root:
            print("Maximum:", tree.maxValueNode(root).key)
        else:
            print("Tree is Empty")

    elif choice == 9:
        print("Height:", tree.height(root))

    elif choice == 10:
        print("Program Terminated")
        break

    else:
        print("Invalid Choice")
