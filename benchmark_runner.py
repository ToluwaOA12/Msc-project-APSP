import time
import tracemalloc
import networkx as nx
import pandas as pd
import random
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

def generate_graph(n, density='sparse'):
    """Generate a random directed graph with specified density."""
    G = nx.DiGraph()
    
    if density == 'sparse':
        edges = n * 4
    else:  # dense
        edges = int(n * (n - 1) * 0.6)  # 60% of maximum possible directed edges
    
    G.add_nodes_from(range(n))
    
    # Generate edges using random selection to avoid infinite loops
    attempts = 0
    max_attempts = edges * 10
    
    while G.number_of_edges() < edges and attempts < max_attempts:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        
        if u != v and not G.has_edge(u, v):
            weight = random.uniform(1.0, 10.0)
            G.add_edge(u, v, weight=weight)
        
        attempts += 1
    
    return G

# Benchmark configuration for MSc dissertation
results = []
test_sizes = [50, 100, 150, 200, 250]
densities = ['sparse', 'dense']

print("Floyd-Warshall Algorithm Performance Benchmark")
print("MSc Dissertation - University of Greenwich")
print("=" * 60)

total_cases = len(test_sizes) * len(densities)
case_num = 0

for size in test_sizes:
    for density in densities:
        case_num += 1
        print(f"[{case_num}/{total_cases}] Testing: {size} nodes, {density} density")
        
        try:
            # Generate test graph
            G = generate_graph(size, density)
            edge_count = G.number_of_edges()
            print(f"    Generated graph: {edge_count} edges")
            
            # Convert to adjacency matrix
            D = nx.to_numpy_array(G, nodelist=sorted(G.nodes), weight='weight', dtype=float)
            
            # Prepare matrix for Floyd-Warshall algorithm
            D[D == 0] = float('inf')  # No edge represented as infinity
            for i in range(size):
                D[i, i] = 0  # Distance from node to itself is zero
            
            # Execute benchmark
            tracemalloc.start()
            start = time.perf_counter()
            
            dist, pred = floyd_warshall(D)
            
            end = time.perf_counter()
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            
            runtime = round(end - start, 4)
            peak_memory_mb = round(peak / (1024 * 1024), 2)
            
            results.append({
                "V": size,
                "Density": density,
                "Edges": edge_count,
                "Runtime (s)": runtime,
                "Peak Memory (MB)": peak_memory_mb
            })
            
            print(f"    Runtime: {runtime}s, Peak Memory: {peak_memory_mb}MB")
            
        except Exception as e:
            print(f"    ERROR: {e}")
            if tracemalloc.is_tracing():
                tracemalloc.stop()
        
        print()

# Generate results
df = pd.DataFrame(results)
df.to_csv("benchmark_results.csv", index=False)

print("=" * 60)
print("BENCHMARK RESULTS")
print("=" * 60)
print(df.to_string(index=False))
print(f"\nResults saved to: benchmark_results.csv")
print(f"Total execution time: {df['Runtime (s)'].sum():.2f} seconds")
print("Benchmark completed successfully!")
