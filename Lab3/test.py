from Algorithms import Graph  # Assuming Graph is correctly implemented with addEdge, DFS, and BFS methods
from matplotlib import pyplot as plt
import random
import time

graphs = []

# Creating graphs and adding edges
for i in range(10):
    g = Graph()  # Create a new Graph instance
    for j in range(10):

        g.addEdge(j, random.randint(0, 9))  # Add edges with random connections
    graphs.append(g)  # Append the graph to the list

timeDFS = []
timeBFS = []
# Iterating over each graph and measuring DFS execution time
for graph in graphs:
    start = time.perf_counter()
    graph.DFS(1)  # Assuming DFS method exists and starts traversal from node 1
    end = time.perf_counter()
    timeDFS.append(end - start)

    start = time.perf_counter()
    graph.bfs(1)  # Assuming BFS method exists and starts traversal from node 1
    end = time.perf_counter()
    timeBFS.append(end - start)


# Plotting the graph
plt.plot(range(1, len(graphs) + 1), timeDFS, label="DFS")
plt.plot(range(1, len(graphs) + 1), timeBFS, label="BFS")
plt.xlabel('Graph Number')
plt.ylabel('Time taken for DFS')
plt.title('Graph Number vs Time taken for DFS')
plt.legend()
plt.show()
