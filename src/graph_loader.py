import json
import numpy as np
import networkx as nx

def load_graph(filename):
    """Load graph from JSON file and return as NetworkX graph and adjacency matrix."""
    with open(filename, 'r') as f:
        data = json.load(f)
    
    nodes = data["nodes"]
    edges = data["edges"]
    
    # Create NetworkX graph
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)
    
    # Create adjacency matrix
    n = len(nodes)
    D = np.full((n, n), np.inf)
    np.fill_diagonal(D, 0)

    for u, v, w in edges:
        D[u][v] = w
    
    return G, D

def create_sample_graph():
    """Create a sample graph for demonstration."""
    # Create a simple 4-node graph
    G = nx.DiGraph()
    G.add_nodes_from([0, 1, 2, 3])
    G.add_edge(0, 1, weight=3)
    G.add_edge(0, 3, weight=6)
    G.add_edge(1, 2, weight=2)
    G.add_edge(2, 3, weight=1)
    G.add_edge(3, 0, weight=4)
    G.add_edge(3, 1, weight=7)
    G.add_edge(3, 2, weight=9)
    
    # Save as JSON
    data = {
        "nodes": list(G.nodes),
        "edges": [(u, v, d['weight']) for u, v, d in G.edges(data=True)]
    }
    
    with open('data/sample_graph.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    return G
