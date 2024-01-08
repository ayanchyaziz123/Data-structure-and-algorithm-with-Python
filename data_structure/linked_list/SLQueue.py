class Node:
    def __init__(self, data):
        # Node constructor initializes a new node with given data
        self.data = data
        self.next = None  # Pointer to the next node, initially set to None
        self.prev = None  # Pointer to the previous node, initially set to None

class Queue:
    def __init__(self):
        # Queue constructor initializes an empty queue with null front and rear
        self.front = None
        self.rear = None

    def push(self, data):
        # Method to push a new node with given data into the queue
        new_node = Node(data)  # Create a new node with the given data

        if self.front is None or self.rear is None:
            # If the queue is empty, set both front and rear to the new node
            self.front = self.rear = new_node
            return

        # If the queue is not empty, adjust pointers for the new node
        self.rear.prev = new_node
        new_node.next = self.rear
        self.rear = new_node

    def traversal(self):
        # Method to traverse and print the elements of the queue
        temp = self.front  # Start traversal from the front of the queue
        while temp is not None:
            print(temp.prev)
            temp = temp.prev  # Move to the previous node

# Creating an instance of the Queue
queue = Queue()

# Pushing elements into the queue
queue.push(10)
queue.push(20)
queue.push(30)

# Traversing and printing the elements of the queue
queue.traversal()
