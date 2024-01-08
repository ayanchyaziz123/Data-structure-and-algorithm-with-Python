from collections import defaultdict

class BreadthFirstSearch:
    def __init__(self) -> None:
        # Constructor initializes a graph using a defaultdict and a list to track visited nodes
        self.graph = defaultdict(list)
        self.visited = []

    def addEdge(self, src: int, dst: int) -> None:
        # Method to add an undirected edge between source and destination nodes
        self.graph[src].append(dst)
        self.graph[dst].append(src)

    def breadthFirstSearch(self, src: int) -> None:
        # Method to perform Breadth-First Search starting from the source node
        queue = []
        queue.append(src)
        self.visited.append(src)

        while queue:
            current_node = queue.pop(0)
            print(current_node, end=" ")

            for neighbor in self.graph[current_node]:
                if neighbor not in self.visited:
                    queue.append(neighbor)
                    self.visited.append(neighbor)

# Example Usage
bfs = BreadthFirstSearch()
bfs.addEdge(0, 1)
bfs.addEdge(0, 2)
bfs.addEdge(2, 3)
bfs.addEdge(1, 3)
bfs.breadthFirstSearch(0)
