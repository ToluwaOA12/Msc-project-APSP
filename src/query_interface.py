import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from graph_loader import load_graph
from floyd_warshall import floyd_warshall, reconstruct_path
from visualizer import plot_heatmap, plot_graph_with_path

class APSPQueryInterface:
    def __init__(self, graph_file):
        """Initialize the query interface with a graph file."""
        print(f"Loading graph from {graph_file}...")
        self.G, self.D = load_graph(graph_file)
        print("Computing all-pairs shortest paths...")
        self.dist, self.pred = floyd_warshall(self.D)
        print("Ready for queries!")
    
    def query_path(self, source, target, visualize=True):
        """Query the shortest path between source and target nodes."""
        # Check if nodes exist
        if source not in self.G.nodes or target not in self.G.nodes:
            print(f"Error: Node {source} or {target} not found in graph.")
            return None, None
        
        # Check if path exists
        if self.dist[source, target] == float('inf'):
            print(f"No path exists from node {source} to node {target}")
            return None, None
        
        # Reconstruct path
        path = reconstruct_path(self.pred, source, target)
        distance = self.dist[source, target]
        
        # Display results
        print(f"\n🔍 Shortest Path Query: {source} → {target}")
        print(f"📍 Path: {' → '.join(map(str, path))}")
        print(f"📏 Distance: {distance}")
        
        # Visualize if requested
        if visualize:
            print("\n📊 Generating visualization...")
            plot_graph_with_path(self.G, path)
        
        return path, distance
    
    def interactive_query(self):
        """Run an interactive query session."""
        print("\n" + "="*50)
        print("🔍 Interactive Shortest Path Query")
        print("Enter 'q' to quit, 'h' for help")
        print("="*50)
        
        while True:
            try:
                user_input = input("\nEnter source node (or command): ").strip()
                
                # Handle commands
                if user_input.lower() == 'q':
                    print("Exiting query interface. Goodbye!")
                    break
                elif user_input.lower() == 'h':
                    self.show_help()
                    continue
                
                source = int(user_input)
                target = int(input("Enter target node: ").strip())
                
                # Query the path
                path, distance = self.query_path(source, target)
                
                if path is not None:
                    # Ask if user wants to see the heatmap
                    show_heatmap = input("\nShow distance matrix heatmap? (y/n): ").strip().lower()
                    if show_heatmap == 'y':
                        plot_heatmap(self.dist)
                
            except ValueError:
                print("⚠️ Please enter valid node numbers or commands.")
            except KeyboardInterrupt:
                print("\n\nExiting query interface. Goodbye!")
                break
            except Exception as e:
                print(f"⚠️ Error: {e}")
    
    def show_help(self):
        """Show help information."""
        print("\n📖 Help:")
        print("  Enter source and target node numbers to query shortest path")
        print("  Commands:")
        print("    q - Quit the query interface")
        print("    h - Show this help message")
        print("  After querying a path, you can choose to see the heatmap")

def main():
    """Main function to run the query interface."""
    print("🎓 MSc Dissertation: All-Pairs Shortest Path Problem")
    print("🔍 Query Interface for Floyd-Warshall Algorithm")
    print("=" * 60)
    
    # Check if graph file is provided
    if len(sys.argv) > 1:
        graph_file = sys.argv[1]
    else:
        graph_file = 'data/sample_graph.json'
        print(f"No graph file specified, using default: {graph_file}")
    
    # Create and run the query interface
    interface = APSPQueryInterface(graph_file)
    interface.interactive_query()

if __name__ == "__main__":
    main()
