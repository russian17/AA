from Algorithms import Algorithms
import matplotlib.pyplot as plt
from time import time
import sys

# Increase the recursion limit, be cautious with this
sys.setrecursionlimit(1000000)  # For example, increasing to 10,000

# Assuming Algorithms class is correctly implemented with addEdge, dfs, bfs methods
# and a way to reset the graph and visited nodes

# Define the metrics for comparison
number_of_nodes = [10, 100, 1000, 10000]
dfs_times = []
bfs_times = []

# Create an instance of the Algorithms class
alg = Algorithms()

# Function to generate a graph
def generate_graph(alg, nodes, edges_per_node):
    alg.reset_graph()  # Assuming this method resets the graph structure
    for i in range(nodes):
        for j in range(1, edges_per_node + 1):  # Ensure edges are added correctly
            alg.addEdge(i, (i + j) % nodes)

# Compare DFS and BFS for varying number of nodes
for nodes in number_of_nodes:
    edges_per_node = max(1, nodes // 10)  # Example relation, adjust based on needs

    # Generate graph
    generate_graph(alg, nodes, edges_per_node)

    # Measure DFS time
    start = time()
    alg.dfs(0)
    dfs_end = time() - start
    dfs_times.append(dfs_end)

    # Reset visited for accurate BFS measurement
    alg.reset_visited()  # Assuming this method resets the visited nodes

    # Measure BFS time
    start = time()
    alg.bfs(0)
    bfs_end = time() - start
    bfs_times.append(bfs_end)

# Plot the results
plt.plot(number_of_nodes, dfs_times, label='DFS Time')
plt.plot(number_of_nodes, bfs_times, label='BFS Time')
plt.xlabel('Number of Nodes')
plt.ylabel('Time (seconds)')
plt.xscale('log')  # Given the wide range of node numbers, a log scale might be appropriate
plt.yscale('log')  # Assuming time differences can be large, adjust if not necessary
plt.title('DFS vs BFS Execution Time')
plt.legend()
plt.show()

