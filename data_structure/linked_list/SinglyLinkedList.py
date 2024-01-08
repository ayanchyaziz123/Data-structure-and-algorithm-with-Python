class ListNode:
    def __init__(self, data) -> None:
        # Node constructor initializes a new node with given data
        self.data = data
        self.next = None  # Pointer to the next node, initially set to None

class SLinkedList:
    def __init__(self):
        # Singly Linked List constructor initializes an empty list with a null head
        self.head = None

    def insertInHead(self, data):
        # Method to insert a new node at the beginning of the linked list
        newNode = ListNode(data)  # Create a new node with the given data
        if self.head is None:
            # If the list is empty, set the new node as the head
            self.head = newNode
            return
        # Otherwise, set the next pointer of the new node to the current head
        newNode.next = self.head
        # Update the head to the new node
        self.head = newNode

    def print_list(self):
        # Method to print the elements of the linked list
        temp = self.head  # Start from the head of the list
        while temp is not None:
            print(temp.data, end=" ")  # Print the data of the current node
            temp = temp.next  # Move to the next node

# Creating an instance of the Singly Linked List
list1 = SLinkedList()

# Inserting elements at the beginning of the list
list1.insertInHead(10)
list1.insertInHead(20)
list1.insertInHead(30)

# Printing the elements of the list
list1.print_list()
