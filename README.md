# Solving and Visualizing the All-Pairs Shortest Paths (APSP) Problem

This repository contains the full source code and experimental artefacts for the MSc dissertation titled "Solving and Visualizing the All-Pairs Shortest Paths (APSP) Problem," submitted for the MSc in Big Data and Business Intelligence at the University of Greenwich.

## Overview

The project implements the Floyd-Warshall algorithm in Python, focusing on creating a pedagogical tool for visualizing the algorithm's step-by-step execution. The system uses NetworkX and NumPy for the core computation and Matplotlib/Seaborn for generating animated visualizations within a Jupyter Notebook environment.

## Structure

- `/src`: Contains the core Python source code for the project modules.
- `/notebooks`: Contains the main `fw_visual_demo.ipynb` Jupyter Notebook.
- `/data`: Contains the synthetic graph data used for experiments.
- `/tests`: Contains the `unittest` or `pytest` test suite.

## Running the Project

### 1. Environment Setup

To replicate the environment, please ensure you have Python 3.11+ installed. Then, run the following commands:

```bash
# Clone the repository
git clone https://github.com/YourUsername/Your-Repo-Name.git
cd Your-Repo-Name

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
/src           → Python modules and core logic /notebooks     → Main Jupyter notebook (fw_visual_demo.ipynb) /data          → Sample graph data for experiments /tests         → Unit tests (if any)

---

## ⚙️ Running the Project

### 1. Environment Setup

Ensure you have **Python 3.11+** installed. Then run:

```bash
# Clone the repository
git clone https://github.com/ToluwaOA12/Msc-project-APSP.git
cd Msc-project-APSP

# Set up a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
---

Citation

If you use this work, please cite the accompanying dissertation:

> **Toluwa O. A.** (2025). *Solving and Visualizing the All-Pairs Shortest Paths (APSP) Problem*. MSc Dissertation, Big Data and Business Intelligence, University of Greenwich.
