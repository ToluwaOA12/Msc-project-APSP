import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from graph_loader import create_sample_graph, load_graph
from floyd_warshall import floyd_warshall, reconstruct_path
from visualizer import plot_heatmap, plot_graph_with_path
from query_interface import APSPQueryInterface

def main():
    print("🎓 MSc Dissertation: All-Pairs Shortest Path Problem")
    print("📊 Floyd-Warshall Algorithm with Visualization")
    print("=" * 60)
    
    # Create sample graph if it doesn't exist
    if not os.path.exists('data/sample_graph.json'):
        print("Creating sample graph...")
        create_sample_graph()
    
    # Menu for user to choose mode
    print("\nChoose mode:")
    print("1. Full demonstration with visualizations")
    print("2. Interactive query interface")
    print("3. Run performance benchmarks")
    
    choice = input("Enter your choice (1-3): ").strip()
    
    if choice == '1':
        run_demonstration()
    elif choice == '2':
        interface = APSPQueryInterface('data/sample_graph.json')
        interface.interactive_query()
    elif choice == '3':
        run_benchmarks()
    else:
        print("Invalid choice. Running demonstration by default.")
        run_demonstration()

def run_demonstration():
    """Run the full demonstration with visualizations."""
    print("\nRunning full demonstration...")
    
    # Load graph
    G, D = load_graph('data/sample_graph.json')
    
    # Run Floyd-Warshall algorithm
    print("Computing all-pairs shortest paths...")
    dist, pred = floyd_warshall(D)
    
    # Display distance matrix
    print("\nDistance Matrix:")
    print(dist)
    
    # Visualize results
    print("\nGenerating visualizations...")
    plot_heatmap(dist, "Distance Matrix Heatmap")
    
    # Example queries
    queries = [(1, 0), (0, 3), (2, 1)]
    for source, target in queries:
        path = reconstruct_path(pred, source, target)
        distance = dist[source, target]
        print(f"\nShortest path from node {source} to node {target}: {path}")
        print(f"Distance: {distance}")
        plot_graph_with_path(G, path)

def run_benchmarks():
    """Run performance benchmarks."""
    print("\nRunning performance benchmarks...")
    from benchmark_runner import run_benchmark
    df = run_benchmark()
    from visualizer import plot_performance_results
    plot_performance_results(df)

if __name__ == "__main__":
    main()
