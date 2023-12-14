from collections import defaultdict
class BreadthFirstSearch:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
        self.visited = []

    def addEdge(self, src: int, dst: int)-> None:
        self.graph[src].append(dst)
        self.graph[dst].append(src)

    def breadthBirstSearch(self, src: int)-> None:
        queue = []
        queue.append(src)
        self.visited.append(src)
        while queue:
            pr = queue.pop(0)
            print(pr, end=" ")
            for ch in self.graph[pr]:
                if(ch not in self.visited):
                    queue.append(ch)
                    self.visited.append(ch)
bfs = BreadthFirstSearch()
bfs.addEdge(0, 1)
bfs.addEdge(0, 2)
bfs.addEdge(2, 3)
bfs.addEdge(1, 3)
bfs.breadthBirstSearch(0)