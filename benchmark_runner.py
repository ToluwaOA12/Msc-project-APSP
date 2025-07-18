import time
import tracemalloc
import networkx as nx
import pandas as pd
from floyd_warshall import floyd_warshall

def generate_graph(n, density='sparse'):
    G = nx.DiGraph()
    if density == 'sparse':
        edges = n * 4
    else:  # dense
        edges = int(n * n * 0.8)
    G.add_nodes_from(range(n))
    while G.number_of_edges() < edges:
        u, v = nx.utils.random_sequence.discrete_sequence(2, 0, n - 1)
        if u != v:
            G.add_edge(u, v, weight=nx.utils.uniform_sequence(1)[0])
    return G

results = []

for size in [100, 200, 300, 400, 500]:
    for density in ['sparse', 'dense']:
        G = generate_graph(size, density)
        D = nx.to_numpy_array(G, nodelist=sorted(G.nodes), weight='weight', dtype=float)
        start = time.perf_counter()
        tracemalloc.start()
        dist, pred = floyd_warshall(G)
        current, peak = tracemalloc.get_traced_memory()
        end = time.perf_counter()
        tracemalloc.stop()

        results.append({
            "V": size,
            "Density": density,
            "Runtime (s)": round(end - start, 4),
            "Peak Memory (MB)": round(peak / (1024 * 1024), 2)
        })

df = pd.DataFrame(results)
df.to_csv("benchmark_results.csv", index=False)
print(df)
