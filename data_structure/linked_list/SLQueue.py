class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def push(self, data):
        new_node = Node(data)
        if(self.front == None or self.rear == None):
            self.front = self.rear = new_node
            return
        #    9 10 20
        self.rear.prev = new_node
        new_node.next = self.rear
        self.rear = new_node

    def travelsal(self):
        temp = self.front
        while(temp!=None):
            print(temp.prev)
            temp = temp.prev    
queue = Queue()
queue.push(10)
queue.push(20)
queue.push(30)
queue.travelsal()
