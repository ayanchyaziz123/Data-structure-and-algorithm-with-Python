from collections import defaultdict

class DepthFirstSearch:
    def __init__(self) -> None:
        # Constructor initializes a graph using a defaultdict and a list to track visited nodes
        self.graph = defaultdict(list)
        self.visited = []

    def addEdge(self, src: int, dst: int) -> None:
        # Method to add an undirected edge between source and destination nodes
        self.graph[src].append(dst)
        self.graph[dst].append(src)

    def depthFirstSearch(self, src: int) -> None:
        # Method to perform Depth-First Search starting from the source node
        for neighbor in self.graph[src]:
            if neighbor not in self.visited:
                print(neighbor, end=" ")
                self.visited.append(neighbor)
                self.depthFirstSearch(neighbor)

# Example Usage
dfs = DepthFirstSearch()
dfs.addEdge(0, 1)
dfs.addEdge(0, 2)
dfs.addEdge(2, 3)
dfs.addEdge(1, 3)
dfs.depthFirstSearch(0)
