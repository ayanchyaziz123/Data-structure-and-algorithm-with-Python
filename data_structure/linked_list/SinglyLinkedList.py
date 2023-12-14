class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
    def insertInHead(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        newNode.next = self.head
        self.head = newNode
    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=" ")
            temp = temp.next

list1 = SLinkedList()
list1.insertInHead(10)
list1.insertInHead(20)
list1.insertInHead(30)
list1.print_list()
