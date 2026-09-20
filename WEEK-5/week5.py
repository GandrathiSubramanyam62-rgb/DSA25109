#G.SUBRAMANYAM
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class SinglyLinkedList:
    def __init__(self):
        self.head = None
    # 1. Create LL
    def create(self):
        n = int(input("Enter number of nodes: "))
        for i in range(n):
            data = int(input("Enter data: "))
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = new_node
    # 2. Insert at beginning
    def insert_begin(self):
        data = int(input("Enter data: "))
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    # 3. Insert at end
    def insert_end(self):
        data = int(input("Enter data: "))
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    # 4. Insert at index
    def insert_index(self):
        index = int(input("Enter index: "))
        data = int(input("Enter data: "))
        if index == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for i in range(index - 1):
            if temp is None:
                print("Invalid index")
                return
            temp = temp.next
        if temp is None:
            print("Invalid index")
            return
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node
    # 5. Delete by value
    def delete_value(self):
        value = int(input("Enter value to delete: "))
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next and temp.next.data != value:
            temp = temp.next
        if temp.next is None:
            print("Value not found")
        else:
            temp.next = temp.next.next
    # 6. Delete previous node
    def delete_previous(self):
        value = int(input("Enter value: "))
        if self.head is None or self.head.next is None:
            print("Previous node cannot be deleted")
            return
        if self.head.next.data == value:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next.next and temp.next.next.data != value:
            temp = temp.next
        if temp.next.next is None:
            print("Value not found or no previous node")
        else:
            temp.next = temp.next.next
    # 7. Delete last node
    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
    # 8. Count nodes
    def count_nodes(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        print("Number of nodes:", count)
    # 9. Display / Traverse
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
# Main program
ll = SinglyLinkedList()
while True:
    print("\n--- SINGLY LINKED LIST ---")
    print("1. Create LL")
    print("2. Insert Begin")
    print("3. Insert End")
    print("4. Insert at Index")
    print("5. Delete by Value")
    print("6. Delete Previous Node")
    print("7. Delete Last Node")
    print("8. Count Nodes")
    print("9. Display")
    print("10. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        ll.create()
    elif choice == 2:
        ll.insert_begin()
    elif choice == 3:
        ll.insert_end()
    elif choice == 4:
        ll.insert_index()
    elif choice == 5:
        ll.delete_value()
    elif choice == 6:
        ll.delete_previous()
    elif choice == 7:
        ll.delete_last()
    elif choice == 8:
        ll.count_nodes()
    elif choice == 9:
        ll.display()
    elif choice == 10:
        print("Program ended")
        break
    else:
        print("Invalid choice")
        #G.Subramanyam
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
  # Create DLL
    def create(self):
        n = int(input("Enter number of nodes: "))
        for i in range(n):
            data = int(input("Enter data: "))
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
            else:
                temp = self.head

                while temp.next:
                    temp = temp.next
                temp.next = new_node
                new_node.prev = temp
    # Insert Begin
    def insert_begin(self):
        data = int(input("Enter data: "))
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
    # Insert End
    def insert_end(self):
        data = int(input("Enter data: "))
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    # Insert at index
    def insert_index(self):
        index = int(input("Enter index: "))
        data = int(input("Enter data: "))
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return
        temp = self.head
        for i in range(index - 1):
            if temp is None:
                print("Invalid index")
                return
            temp = temp.next
        if temp is None:
            print("Invalid index")
            return
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node
    # Delete by value
    def delete_value(self):
        value = int(input("Enter value to delete: "))
        temp = self.head
        while temp and temp.data != value:
            temp = temp.next
        if temp is None:
            print("Value not found")
            return
        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next
        if temp.next:
            temp.next.prev = temp.prev
    # Delete previous node
    def delete_previous(self):
        value = int(input("Enter value: "))
        temp = self.head
        while temp and temp.data != value:
            temp = temp.next
        if temp is None or temp.prev is None:
            print("Previous node cannot be deleted")
            return
        previous = temp.prev

        if previous.prev:
            previous.prev.next = temp
        else:
            self.head = temp

        temp.prev = previous.prev

    # Delete last
    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        if temp.prev:
            temp.prev.next = None
        else:
            self.head = None

    # Count
    def count_nodes(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)

    # Display
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


dll = DoublyLinkedList()
while True:
    print("\n--- DOUBLY LINKED LIST ---")
    print("1. Create LL")
    print("2. Insert Begin")
    print("3. Insert End")
    print("4. Insert at Index")
    print("5. Delete by Value")
    print("6. Delete Previous Node")
    print("7. Delete Last Node")
    print("8. Count Nodes")
    print("9. Display")
    print("10. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        dll.create()
    elif choice == 2:
        dll.insert_begin()
    elif choice == 3:
        dll.insert_end()
    elif choice == 4:
        dll.insert_index()
    elif choice == 5:
        dll.delete_value()
    elif choice == 6:
        dll.delete_previous()
    elif choice == 7:
        dll.delete_last()
    elif choice == 8:
        dll.count_nodes()
    elif choice == 9:
        dll.display()
    elif choice == 10:
        print("Program ended")
        break
    else:
        print("Invalid choice")
#G.subramanyam
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Create CLL
    def create(self):
        n = int(input("Enter number of nodes: "))

        for i in range(n):
            data = int(input("Enter data: "))
            self.insert_end_value(data)

    def insert_end_value(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    # Insert Begin
    def insert_begin(self):
        data = int(input("Enter data: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

    # Insert End
    def insert_end(self):
        data = int(input("Enter data: "))
        self.insert_end_value(data)

    # Insert Index
    def insert_index(self):
        index = int(input("Enter index: "))
        data = int(input("Enter data: "))

        if self.head is None:
            if index == 0:
                self.head = Node(data)
                self.head.next = self.head
            else:
                print("Invalid index")
            return

        if index == 0:
            self.insert_begin_data(data)
            return

        temp = self.head

        for i in range(index - 1):
            temp = temp.next

            if temp == self.head:
                print("Invalid index")
                return

        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

    def insert_begin_data(self, data):
        new_node = Node(data)

        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

    # Delete by value
    def delete_value(self):
        value = int(input("Enter value to delete: "))

        if self.head is None:
            print("List is empty")
            return

        current = self.head
        previous = None

        while True:
            if current.data == value:
                break

            previous = current
            current = current.next

            if current == self.head:
                print("Value not found")
                return

        # Only one node
        if current == self.head and current.next == self.head:
            self.head = None
            return

        # Delete head
        if current == self.head:
            last = self.head

            while last.next != self.head:
                last = last.next

            self.head = self.head.next
            last.next = self.head

        else:
            previous.next = current.next

    # Delete previous node
    def delete_previous(self):
        value = int(input("Enter value: "))

        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            print("Previous node cannot be deleted")
            return

        current = self.head
        previous = None
        before_previous = None

        while True:
            if current.data == value:
                break

            before_previous = previous
            previous = current
            current = current.next

            if current == self.head:
                print("Value not found")
                return

        # Previous node is head
        if previous == self.head:
            last = self.head

            while last.next != self.head:
                last = last.next

            self.head = self.head.next
            last.next = self.head

        else:
            before_previous.next = current

    # Delete last
    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head

        while temp.next.next != self.head:
            temp = temp.next

        temp.next = self.head

    # Count
    def count_nodes(self):
        if self.head is None:
            print("Number of nodes: 0")
            return

        count = 0
        temp = self.head

        while True:
            count += 1
            temp = temp.next

            if temp == self.head:
                break

        print("Number of nodes:", count)

    # Display
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(back to head)")


cll = CircularLinkedList()

while True:
    print("\n--- CIRCULAR LINKED LIST ---")
    print("1. Create LL")
    print("2. Insert Begin")
    print("3. Insert End")
    print("4. Insert at Index")
    print("5. Delete by Value")
    print("6. Delete Previous Node")
    print("7. Delete Last Node")
    print("8. Count Nodes")
    print("9. Display")
    print("10. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        cll.create()

    elif choice == 2:
        cll.insert_begin()

    elif choice == 3:
        cll.insert_end()

    elif choice == 4:
        cll.insert_index()

    elif choice == 5:
        cll.delete_value()

    elif choice == 6:
        cll.delete_previous()

    elif choice == 7:
        cll.delete_last()

    elif choice == 8:
        cll.count_nodes()

    elif choice == 9:
        cll.display()

    elif choice == 10:
        print("Program ended")
        break

    else:
        print("Invalid choice")
