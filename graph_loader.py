import json
import numpy as np

def load_graph(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    
    nodes = data["nodes"]
    edges = data["edges"]
    
    n = len(nodes)
    D = np.full((n, n), np.inf)
    np.fill_diagonal(D, 0)

    for u, v, w in edges:
        D[u][v] = w

    return D
