class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.length = 0
    def push(self, data):
        self.length += 1
        new_node = Node(data)
        if(self.head is None):
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    def pop(self):
        self.head = self.head.next  
        self.length-=1
    def len(self):
        return self.length    
    def traversal(self):
        temp = self.head    
        while temp!= None:
            print(temp.data)
            temp = temp.next;      

obj = Stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.pop()

obj.traversal()
print(obj.len())
