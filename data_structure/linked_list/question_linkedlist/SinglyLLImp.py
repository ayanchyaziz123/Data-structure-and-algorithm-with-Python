class Node:
    def __init__(self, data)-> None:
        self.data = data
        self.next = None    

class SinglyLLImp:
    def __init__(self):
        self.head = None
    def addNode(self, data)-> None:
        new_node = Node(data)
        if(self.head is None):
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    def getHead(self):
        return self.head    