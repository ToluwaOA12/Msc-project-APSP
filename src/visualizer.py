import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

def plot_heatmap(D, title="Distance Matrix Heatmap"):
    """Plot distance matrix as a heatmap."""
    plt.figure(figsize=(10, 8))
    plt.imshow(D, cmap='viridis', interpolation='nearest')
    plt.colorbar(label='Distance')
    plt.title(title)
    plt.xlabel('Target Node')
    plt.ylabel('Source Node')
    plt.show()

def plot_graph_with_path(G, path=None, pos=None):
    """Plot the graph with an optional highlighted path."""
    if pos is None:
        pos = nx.spring_layout(G)
    
    plt.figure(figsize=(12, 8))
    
    # Draw all nodes and edges
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edge_color='gray', alpha=0.5)
    
    # Draw edge weights
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    
    # Highlight path if provided
    if path:
        path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, 
                              edge_color='red', width=3)
        nx.draw_networkx_nodes(G, pos, nodelist=path, 
                              node_color='red', node_size=500)
    
    plt.title("Graph with Shortest Path Highlighted")
    plt.axis('off')
    plt.show()

def plot_performance_results(df):
    """Plot performance benchmark results."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    # Runtime plot
    for density in df['Density'].unique():
        subset = df[df['Density'] == density]
        ax1.plot(subset['V'], subset['Runtime (s)'], 
                marker='o', label=f'{density} density')
    ax1.set_xlabel('Number of Nodes')
    ax1.set_ylabel('Runtime (seconds)')
    ax1.set_title('Runtime vs Graph Size')
    ax1.legend()
    ax1.grid(True)
    
    # Memory plot
    for density in df['Density'].unique():
        subset = df[df['Density'] == density]
        ax2.plot(subset['V'], subset['Peak Memory (MB)'], 
                marker='s', label=f'{density} density')
    ax2.set_xlabel('Number of Nodes')
    ax2.set_ylabel('Peak Memory (MB)')
    ax2.set_title('Memory Usage vs Graph Size')
    ax2.legend()
    ax2.grid(True)
    
    plt.tight_layout()
    plt.show()
