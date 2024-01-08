class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, data) -> None:
        self.root = Node(data)

    def getHead(self) -> Node:
        return self.root

    def insertRec(self, root: Node, val: int) -> Node:
        if root is None:
            return Node(val)
        if root.data > val:
            root.left = self.insertRec(root.left, val)
        elif root.data < val:
            root.right = self.insertRec(root.right, val)
        return root  # Don't forget to return the root after recursive calls

    def search(self, root: Node, key: int) -> None:
        if root is None or root.data == key:
            return root
        print(root.data, end=" ")
        if root.data < key:
            return self.search(root.right, key)
        elif root.data > key:
            return self.search(root.left, key)

# Example Usage
bst = BinarySearchTree(10)
root = bst.getHead()
bst.insertRec(root, 20)
bst.insertRec(root, 9)
bst.insertRec(root, 8)
bst.insertRec(root, 11)

# Perform search and print the nodes visited
bst.search(root, 11)
