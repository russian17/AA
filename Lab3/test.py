from Algorithms import Algorithms
import matplotlib.pyplot as plt
from time import time

# create metrics for comparison DFS and BFS
number_of_nodes = [10, 100, 1000, 10000]
number_of_edges = [10, 100, 1000, 10000]
number_of_edges_per_node = [1, 10, 100, 1000]

# metrics for comparison of DFS and BFS
time_of_algorithms = []
nodes_visited = []

# create an instance of the Algorithms class
alg = Algorithms()

# going trough all the metrics and comparing DFS and BFS
for nodes in number_of_nodes:
    for edges in number_of_edges:
        for edges_per_node in number_of_edges_per_node:
            # create a graph with the given parameters
            for i in range(nodes):
                for j in range(edges_per_node):
                    alg.addEdge(i, (i + j) % nodes)
            # measure the time of DFS
            start = time()
            alg.dfs(0)
            end = time()

            # measure the time of BFS
            start = time()
            alg.bfs(0)
            end = time()
            time_of_algorithms['BFS'] = end - start





# plot the results