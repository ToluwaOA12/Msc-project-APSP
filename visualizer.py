import matplotlib.pyplot as plt
import numpy as np

def plot_heatmap(D):
    plt.imshow(D, cmap='viridis', interpolation='nearest')
    plt.colorbar()
    plt.title("Distance Matrix Heatmap")
    plt.show()
