# Uniqueness in Deep Neural Networks  
*The Inevitable Singularity of Learning Trajectories*  

## 📄 Paper  
**[Full Preprint](./Uniqueness_in_Deep_Neural_Networks__The_Inevitable_Singularity_of_Learning_Trajectories.pdf)**  

## 🧠 Abstract  
This repository accompanies the paper **"Uniqueness in Deep Neural Networks: The Inevitable Singularity of Learning Trajectories"** by Haamed Ghiassian.  

We establish fundamental **physical and mathematical constraints** on parameter-level reproducibility in deep neural networks, proving three impossibility theorems:  

1. **Dynamical Impossibility (Chaotic Divergence)**  
   Gradient-based training exhibits **positive Lyapunov exponents**, causing exponential sensitivity to initial conditions.  

2. **Thermodynamic Impossibility (Irreversible Learning)**  
   The learning process is a thermodynamically **irreversible non-equilibrium process** with strictly positive entropy production.  

3. **Topological Impossibility (Topological Distinctness)**  
   Different training trajectories occupy **distinct topological equivalence classes** in parameter space.  

These results collectively imply that **each trained neural network is structurally unique with probability one**, establishing inherent limits to exact reproducibility in deep learning.  

**Keywords:**  
Deep Neural Networks, Physics of Learning, Chaotic Dynamics, Information Theory, Topology, Learning Trajectories, Uniqueness  

## 🚀 Quickstart  
To replicate the theoretical and experimental results:  

```bash
git clone https://github.com/HaAmedghiassian/uniq-nets.git
cd uniq-nets
conda env create -f environment.yml
conda activate uniq-nets
python -m experiments.01_lyapunov.simulate --config experiments/01_lyapunov/config.yaml
```

## 📦 PyPI Installation

The package is available on PyPI for easy installation:

```bash
# Install minimal version (CPU)
pip install uniq-nets

# Or install with Theorem 1 dependencies
pip install "uniq-nets[lyapunov]"

# For development (testing, formatting, etc.)
pip install "uniq-nets[dev]"

# Install in development mode from source
git clone https://github.com/HaAmedghiassian/uniq-nets.git
cd uniq-nets
pip install -e .
```

**Note on PyTorch version:**  
The default installation uses PyTorch CPU. For GPU support, install PyTorch separately:
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

**Version 0.0.1** is an initial release for name reservation and project setup.  
Full functionality (Theorems 1-3 implementations) will be available in version 0.1.0.

## 🎯 Quick Start Example

```python
import uniq_nets

# Check version
print(f"Using uniq-nets v{uniq_nets.__version__}")

# The package is under active development
# Full functionality coming in future releases
```

## Repository Structure

```
uniq-nets/
├── 📜 README.md                 # This file
├── 📄 Uniqueness_in_Deep_Neural_Networks__The_Inevitable_Singularity_of_Learning_Trajectories.pdf   # Main paper (PDF)
├── 📜 pyproject.toml            # Project configuration and dependencies
├── 📜 requirements-minimal.txt  # Minimal pip requirements for quick install
├── 📜 environment.yml           # Conda environment for reproducibility
├── 📜 LICENSE                   # MIT License
│
├── 📂 uniq_nets/                # Main Python package
│   └── 📜 __init__.py           # Package initialization and metadata
│
├── 📂 theory/                   # Theoretical foundations
│   ├── 📁 theorem_1_dynamical/  # Theorem 1: Chaotic Divergence
│   │   ├── 📜 theorem_1_math.tex    # Mathematical formulation
│   │   ├── 📓 theorem_1_dynamical.ipynb   # Interactive notebook
│   │   └── 📜 README.md          # Theorem-specific documentation
│   ├── 📁 theorem_2_thermodynamic/  # Theorem 2: Thermodynamic Irreversibility
│   │   ├── 📜 theorem_2_math.tex    # Mathematical formulation
│   │   ├── 📓 theorem_2_thermodynamic.ipynb  # Interactive notebook
│   │   └── 📜 README.md          # Theorem-specific documentation
│   └── 📁 theorem_3_topological/  # Theorem 3: Topological Distinctness
│       ├── 📜 theorem_3_math.tex    # Mathematical formulation
│       ├── 📓 theorem_3_topological.ipynb  # Interactive notebook
│       └── 📜 README.md          # Theorem-specific documentation
│
├── 📂 experiments/              # Numerical experiments
│   ├── 📁 01_lyapunov/         # Lyapunov exponent estimation
│   │   ├── 📜 simulate.py      # Simulation code
│   │   ├── 📜 config.yaml      # Hyperparameters
│   │   └── 📊 results/         # Output plots/data
│   ├── 📁 02_entropy/          # Entropy production experiments
│   └── 📁 03_topology/         # Topological data analysis
│
└── 📂 assets/                   # All non-code resources
    ├── 📁 figures/             # Paper figures (high-quality)
    │   ├── figure_1.png
    │   ├── figure_2.pdf
    │   └── ...
    ├── 📁 diagrams/            # Supplementary schematic diagrams
    ├── 📁 data_samples/        # Example datasets for demonstration
    └── 📁 media/               # Videos and other multimedia content
```

## Installation

Create and activate the Conda environment:

```bash
conda env create -f environment.yml
conda activate uniq-nets
```

Or install dependencies manually:

```bash
pip install jax jaxlib numpy scipy matplotlib seaborn torch torchvision scikit-learn tqdm gudhi
```

## Theory

The `theory/` directory contains three main theorems, each with its own folder containing mathematical formulations and documentation:

### Theorem 1: Dynamical Impossibility (Chaotic Divergence)
Located in `theory/theorem_1_dynamical/`:
- `theorem_1_math.tex`: Complete mathematical proof using Lyapunov exponents and dynamical systems theory
- `theorem_1_dynamical.ipynb`: Interactive Jupyter notebook with derivations and visualizations
- `README.md`: Theorem-specific documentation, assumptions, and implications

### Theorem 2: Thermodynamic Impossibility (Irreversible Learning)
Located in `theory/theorem_2_thermodynamic/`:
- `theorem_2_math.tex`: Complete mathematical proof using stochastic thermodynamics and information theory
- `theorem_2_thermodynamic.ipynb`: Interactive Jupyter notebook with derivations and visualizations
- `README.md`: Theorem-specific documentation, assumptions, and implications

### Theorem 3: Topological Impossibility (Topological Distinctness)
Located in `theory/theorem_3_topological/`:
- `theorem_3_math.tex`: Complete mathematical proof using persistent homology and high-dimensional geometry
- `theorem_3_topological.ipynb`: Interactive Jupyter notebook with derivations and visualizations
- `README.md`: Theorem-specific documentation, assumptions, and implications

Each theorem folder includes:
- Formal mathematical statements and proofs
- Visualizations of key concepts
- Connections to empirical observations
- Detailed assumptions and boundary conditions

## Experiments

The `experiments/` directory contains reproducible numerical simulations:

### 1. Lyapunov Exponents (`01_lyapunov/`)
Estimates maximal Lyapunov exponents for different architectures using the Benettin algorithm.

```bash
python -m experiments.01_lyapunov.simulate --config experiments/01_lyapunov/config.yaml
```

### 2. Entropy Production (`02_entropy/`)
Computes entropy production rates during training using discrete-time stochastic thermodynamics.

```bash
python -m experiments.02_entropy.simulate --config experiments/02_entropy/config.yaml
```

### 3. Topological Analysis (`03_topology/`)
Applies persistent homology to training trajectories to compute Wasserstein distances between persistence diagrams.

```bash
python -m experiments.03_topology.simulate --config experiments/03_topology/config.yaml
```

Each experiment includes:
- Clean, modular Python code
- Configuration files for hyperparameters
- Visualization scripts
- Pre-computed results for verification

## Citation

If you use this work, please cite:

```bibtex
@article{ghiassian2026uniqueness,
  title={Uniqueness in Deep Neural Networks: The Inevitable Singularity of Learning Trajectories},
  author={Ghiassian, Haamed},
  journal={zenodo preprint},
  year={2026},
  url={https://github.com/HaAmedghiassian/uniq-nets}
}
```

## License

MIT License. See LICENSE file for details.

## Contact

For questions or discussions, please open an issue on GitHub or contact the author directly.
```
haamedghiasian@gmail.com
```
