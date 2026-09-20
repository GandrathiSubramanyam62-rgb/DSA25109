#G.subramanyam
stack = []
MAX = 5
def push():
    if len(stack) == MAX:
        print("Stack Overflow")
    else:
        data = int(input("Enter data: "))
        stack.append(data)
        print(data, "pushed into stack")
def pop():
    if len(stack) == 0:
        print("Stack Underflow")
    else:
        data = stack.pop()
        print(data, "popped from stack")
def peek():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top element:", stack[-1])
def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack:", stack[::-1])
while True:
    print("\n--- STACK USING ARRAY ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    elif choice == 5:
        print("Program ended")
        break
    else:
        print("Invalid choice")
#G.Subramanyam
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
  # PUSH
    def push(self):
        data = int(input("Enter data: "))
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(data, "pushed into stack")
    # POP
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return
        data = self.top.data
        self.top = self.top.next
        print(data, "popped from stack")
    # PEEK
    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element:", self.top.data)

    # DISPLAY
    def display(self):
        if self.top is None:
            print("Stack is empty")
            return
        temp = self.top
        print("Stack:", end=" ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
stack = Stack()
while True:
    print("\n--- STACK USING LINKED LIST ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        stack.push()
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        stack.peek()
    elif choice == 4:
        stack.display()
    elif choice == 5:
        print("Program ended")
        break
    else:
        print("Invalid choice")
