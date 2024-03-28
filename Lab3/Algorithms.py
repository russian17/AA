from collections import deque

class Algorithms:
    def __init__(self):
        self.graph = {}
        self.visited = set()

    def addEdge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:  # Ensure all vertices are in the graph
            self.graph[v] = []
        self.graph[u].append(v)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        for neighbor in self.graph.get(start, []):  # Safely get neighbors or an empty list
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                # Ensure only unvisited neighbors are queued
                queue.extend([n for n in self.graph[vertex] if n not in visited])

    #def printGraph(self):
     #   for k, v in self.graph.items():
      #      print(f"{k}: {v}")

    def get_visited(self):
        return self.visited

    def reset_graph(self):
        self.graph = {}

    def reset_visited(self):
        self.visited = set()
