class Node:
    def __init__(self):
        # Node constructor initializes a node with an array for 26 children (one for each alphabet letter)
        self.children = [None for _ in range(26)]
        self.isEndWord = False  # Flag to indicate if the current node marks the end of a word

class Trie:
    def __init__(self):
        # Trie constructor initializes an empty trie with a root node
        self.root = Node()

    def insert(self, word):
        # Method to insert a word into the trie
        root = self.root  # Start from the root
        for char in word:
            index = ord(char) - ord('a')  # Calculate the index for the current character
            if root.children[index] is None:
                root.children[index] = Node()  # Create a new node if it doesn't exist
            root = root.children[index]  # Move to the next node
        root.isEndWord = True  # Mark the end of the inserted word

    def search(self, word):
        # Method to search for a word in the trie
        root = self.root  # Start from the root
        for char in word:
            index = ord(char) - ord('a')  # Calculate the index for the current character
            if root.children[index] is None and not root.isEndWord:
                return False  # If the current character is not found, return False
            root = root.children[index]  # Move to the next node
        return True  # Return True if the entire word is found

# Example Usage
words = ["ayan", "nakib", "ayanchy"]
trie = Trie()
for word in words:
    trie.insert(word)
print(trie.search("ayanchy"))
