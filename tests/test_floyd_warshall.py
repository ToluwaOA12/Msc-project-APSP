import unittest
import numpy as np
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from floyd_warshall import floyd_warshall, reconstruct_path

class TestFloydWarshall(unittest.TestCase):
    def test_simple_graph(self):
        """Test a simple graph with known results."""
        D = np.array([
            [0, 3, np.inf, 5],
            [2, 0, np.inf, 4],
            [np.inf, 1, 0, np.inf],
            [np.inf, np.inf, 2, 0]
        ])
        dist, pred = floyd_warshall(D)
        
        # Test known shortest paths
        self.assertEqual(dist[0, 2], 6)  # Path 0->1->2
        self.assertEqual(dist[1, 3], 4)  # Direct path
        self.assertEqual(dist[2, 0], 7)  # Path 2->1->0
        
    def test_unreachable_nodes(self):
        """Test a graph with unreachable nodes."""
        D = np.array([
            [0, 1, np.inf],
            [np.inf, 0, np.inf],
            [np.inf, np.inf, 0]
        ])
        dist, pred = floyd_warshall(D)
        
        # Test unreachable nodes
        self.assertEqual(dist[0, 2], np.inf)
        self.assertEqual(dist[1, 2], np.inf)
        self.assertEqual(dist[2, 0], np.inf)
        
    def test_negative_weights(self):
        """Test a graph with negative weights (but no negative cycles)."""
        D = np.array([
            [0, 1, np.inf],
            [np.inf, 0, -2],
            [np.inf, np.inf, 0]
        ])
        dist, pred = floyd_warshall(D)
        
        # Test shortest path with negative weight
        self.assertEqual(dist[0, 2], -1)  # Path 0->1->2
        
    def test_path_reconstruction(self):
        """Test path reconstruction functionality."""
        D = np.array([
            [0, 1, np.inf],
            [np.inf, 0, 2],
            [np.inf, np.inf, 0]
        ])
        dist, pred = floyd_warshall(D)
        
        # Test path reconstruction
        path = reconstruct_path(pred, 0, 2)
        self.assertEqual(path, [0, 1, 2])

if __name__ == '__main__':
    unittest.main()
