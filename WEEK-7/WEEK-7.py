
  #G.Subramanyam
MAX = 5
queue = []
front = 0
rear = -1
def enqueue():
    global rear
    if rear == MAX - 1:
        print("Queue Overflow")
    else:
        value = int(input("Enter element: "))
        queue.append(value)
        rear += 1
        print("Element inserted successfully")
def dequeue():
    global front
    if front > rear:
        print("Queue Underflow")
    else:
        print("Deleted element:", queue[front])
        front +=1
def peek():
    if front > rear:
        print("Queue is empty")
    else:
        print("Front element:", queue[front])
def display():
    if front > rear:
        print("Queue is empty")
    else:
        print("Queue elements:")
        for i in range(front, rear + 1):
            print(queue[i], end=" ")
        print()
while True:
    print("\n--- QUEUE USING ARRAY ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    elif choice == 5:
        print("Program terminated")
        break
    else:
        print("Invalid choice")
#G.Subramanyam
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
front = None
rear = None
def enqueue():
    global front, rear
    value = int(input("Enter element: "))
    new_node = Node(value)
    if rear is None:
        front = rear = new_node
    else:
        rear.next = new_node
        rear = new_node
    print("Element inserted successfully")
def dequeue():
    global front, rear
    if front is None:
        print("Queue Underflow")
    else:
        print("Deleted element:", front.data)
        front = front.next
        if front is None:
            rear = None
def peek():
    if front is None:
        print("Queue is empty")
    else:
        print("Front element:", front.data)
def display():
    if front is None:
        print("Queue is empty")
    else:
        temp = front
        print("Queue elements:")
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()
while True:
    print("\n--- QUEUE USING LINKED LIST ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    elif choice == 5:
        print("Program terminated")
        break
    else:
        print("Invalid choice")
#G.Subramanyam
MAX = 5
queue = [None] * MAX
front = -1
rear = -1
def enqueue():
    global front, rear
    if (rear + 1) % MAX == front:
        print("Circular Queue Overflow")
        return
    value = int(input("Enter element: "))
    if front == -1:
        front = 0
        rear = 0
    else:
        rear = (rear + 1) % MAX
    queue[rear] = value
    print("Element inserted successfully")
def dequeue():
    global front, rear
    if front == -1:
        print("Circular Queue Underflow")
        return
    print("Deleted element:", queue[front])
    queue[front] = None
    if front == rear:
        front = -1
        rear = -1
    else:
        front = (front + 1) % MAX
def peek():
    if front == -1:
        print("Queue is empty")
    else:
        print("Front element:", queue[front])
def display():
    if front == -1:
        print("Queue is empty")
        return
    print("Circular Queue elements:")
    i = front
    while True:
        print(queue[i], end=" ")
        if i == rear:
            break
        i = (i + 1) % MAX
    print()
while True:
    print("\n--- CIRCULAR QUEUE ---")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        peek()
    elif choice == 4:
        display()
    elif choice == 5:
        print("Program terminated")
        break
    else:
        print("Invalid choice")
