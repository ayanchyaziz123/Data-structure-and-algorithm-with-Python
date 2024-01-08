class Node:
    def __init__(self, data):
        # Node constructor initializes a new node with given data
        self.data = data
        self.next = None  # Pointer to the next node, initially set to None

class Stack:
    def __init__(self):
        # Stack constructor initializes an empty stack with null head and length 0
        self.head = None
        self.length = 0

    def push(self, data):
        # Method to push a new node with given data onto the stack
        self.length += 1  # Increment the length of the stack
        new_node = Node(data)  # Create a new node with the given data

        if self.head is None:
            # If the stack is empty, set the head to the new node
            self.head = new_node
            return

        # If the stack is not empty, adjust pointers for the new node
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        # Method to pop the top element from the stack
        if self.head is not None:
            self.head = self.head.next  # Move to the next node
            self.length -= 1  # Decrement the length of the stack

    def len(self):
        # Method to get the length of the stack
        return self.length

    def traversal(self):
        # Method to traverse and print the elements of the stack
        temp = self.head  # Start traversal from the head of the stack
        while temp is not None:
            print(temp.data)
            temp = temp.next  # Move to the next node

# Creating an instance of the Stack
obj = Stack()

# Pushing elements onto the stack
obj.push(10)
obj.push(20)
obj.push(30)

# Popping an element from the stack
obj.pop()

# Traversing and printing the elements of the stack
obj.traversal()

# Printing the length of the stack
print(obj.len())
