class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def insertRec(root, val):
        mew_node = Node()
        if(root.data > val):
            root.left = insertRec(root.left, val)
        elif(root.data < val):
            root.right = insertRec(root.right, val)  
