from collections import defaultdict
class DepthFirstSearch:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
        self.visited = []

    def addEdge(self, src: int, dst: int)-> None:
        self.graph[src].append(dst)
        self.graph[dst].append(src)

    def depthFirstSearch(self, src: int)-> None:
        for ch in self.graph[src]:
            if ch not in self.visited:
                print(ch, end=" ")
                self.visited.append(ch)
                self.depthFirstSearch(ch)

bfs = DepthFirstSearch()
bfs.addEdge(0, 1)
bfs.addEdge(0, 2)
bfs.addEdge(2, 3)
bfs.addEdge(1, 3)
bfs.depthFirstSearch(0)