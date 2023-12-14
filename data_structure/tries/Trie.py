class Node:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isEndWord = False

class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self, str):
        root = self.root
        for i in range(0, len(str)):
            ind = ord(str[i]) - ord('a')
            if root.children[ind] == None:
                root.children[ind] = Node()
            root = root.children[ind]            
        root.isEndWord = True

    def search(self, str):
        root = self.root
        for i in range(0, len(str)):
            ind = ord(str[i]) - ord('a')
            if(root.children[ind] == None and root.isEndWord == False):
                return False
            root = root.children[ind]
        return True    

words = ["ayan", "nakib", "ayanchy"]
trie = Trie()
for word in words:
    trie.insert(word)    
print(trie.search("ayanchy"))   