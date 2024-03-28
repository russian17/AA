from collections import deque

# implementation of DFS and BFS
class Algorithms:
    def __init__(self):
        self.graph = {}
        self.visited = set()

    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start):
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                stack.extend(self.graph[node])

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex, end=" ")
                queue.extend(set(self.graph[vertex]) - visited)

    def printGraph(self):
        for k, v in self.graph.items():
            print(k, v)

    def visited(self):
        return self.visited