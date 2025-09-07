import numpy as np

def floyd_warshall(D):
    """
    Floyd-Warshall algorithm implementation.
    
    Args:
        D: n x n adjacency matrix with np.inf for missing edges and 0 on diagonal
        
    Returns:
        tuple: (distance_matrix, predecessor_matrix)
    """
    n = D.shape[0]
    
    # Initialize distance and predecessor matrices
    dist = D.copy()
    pred = np.full((n, n), -1, dtype=int)
    
    # Initialize predecessors for direct edges
    for i in range(n):
        for j in range(n):
            if i != j and np.isfinite(dist[i, j]):
                pred[i, j] = i
    
    # Floyd-Warshall main algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i, k] + dist[k, j] < dist[i, j]:
                    dist[i, j] = dist[i, k] + dist[k, j]
                    pred[i, j] = pred[k, j]
    
    return dist, pred

def reconstruct_path(pred, i, j):
    """Reconstruct path from predecessor matrix."""
    if pred[i, j] == -1:
        return []
    path = [j]
    while j != i:
        j = pred[i, j]
        path.append(j)
    return path[::-1]
