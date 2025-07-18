from graph_loader import load_graph
from floyd_warshall import floyd_warshall
from visualizer import plot_heatmap

# Load graph
graph = load_graph('sample_graph.json')

# Solve APSP
distance_matrix, predecessor_matrix = floyd_warshall(graph)

# Visualize result
plot_heatmap(distance_matrix)
