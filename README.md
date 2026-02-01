# Uniqueness in Deep Neural Networks  
*The Inevitable Singularity of Learning Trajectories*  

## 📄 Paper  
**[Full Preprint](./Uniqueness_in_Deep_Neural_Networks__The_Inevitable_Singularity_of_Learning_Trajectories.pdf)**  
**DOI:** [10.5281/zenodo.18433336](https://doi.org/10.5281/zenodo.18433336)

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

**Note:** This repository is under active development. Version 0.0.1 is an initial release establishing the project structure and package infrastructure. Full experimental implementations will be available in upcoming releases.

To set up the development environment:

```bash
git clone https://github.com/HaAmedghiassian/uniq-nets.git
cd uniq-nets
conda env create -f environment.yml
conda activate uniq-nets
```

*Experimental simulations will be available in future releases.*

## 📦 PyPI Installation

The package is available on PyPI for easy installation:

```bash
# Install minimal version (CPU) - v0.0.1 (project infrastructure only)
pip install uniq-nets

# For future releases with Theorem 1 dependencies:
# pip install "uniq-nets[lyapunov]"

# For development (testing, formatting, etc.):
# pip install "uniq-nets[dev]"

# Install in development mode from source:
git clone https://github.com/HaAmedghiassian/uniq-nets.git
cd uniq-nets
pip install -e .
```

**Note on PyTorch version:**  
The default installation uses PyTorch CPU. For GPU support, install PyTorch separately:
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

**Current Status:**  
Version 0.0.1 establishes the project infrastructure. Full functionality (Theorems 1-3 implementations) will be available in version 0.1.0+.

## 🎯 Package Overview

```python
import uniq_nets

# Check version
print(f"Using uniq-nets v{uniq_nets.__version__}")

# Package is under active development
# Full functionality will be implemented in upcoming releases
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
│   │   ├── 📓 theorem_1_dynamical.ipynb   # Interactive notebook (planned)
│   │   └── 📜 README.md          # Theorem-specific documentation
│   ├── 📁 theorem_2_thermodynamic/  # Theorem 2: Thermodynamic Irreversibility
│   │   ├── 📜 theorem_2_math.tex    # Mathematical formulation
│   │   ├── 📓 theorem_2_thermodynamic.ipynb  # Interactive notebook (planned)
│   │   └── 📜 README.md          # Theorem-specific documentation
│   └── 📁 theorem_3_topological/  # Theorem 3: Topological Distinctness
│       ├── 📜 theorem_3_math.tex    # Mathematical formulation
│       ├── 📓 theorem_3_topological.ipynb  # Interactive notebook (planned)
│       └── 📜 README.md          # Theorem-specific documentation
│
├── 📂 experiments/              # Numerical experiments (under development)
│   ├── 📁 01_lyapunov/         # Lyapunov exponent estimation (planned)
│   │   ├── 📜 simulate.py      # Simulation code (planned)
│   │   ├── 📜 config.yaml      # Hyperparameters (planned)
│   │   └── 📊 results/         # Output plots/data (planned)
│   ├── 📁 02_entropy/          # Entropy production experiments (planned)
│   └── 📁 03_topology/         # Topological data analysis (planned)
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
- `theorem_1_dynamical.ipynb`: Interactive Jupyter notebook with derivations and visualizations *(planned)*
- `README.md`: Theorem-specific documentation, assumptions, and implications

### Theorem 2: Thermodynamic Impossibility (Irreversible Learning)
Located in `theory/theorem_2_thermodynamic/`:
- `theorem_2_math.tex`: Complete mathematical proof using stochastic thermodynamics and information theory
- `theorem_2_thermodynamic.ipynb`: Interactive Jupyter notebook with derivations and visualizations *(planned)*
- `README.md`: Theorem-specific documentation, assumptions, and implications

### Theorem 3: Topological Impossibility (Topological Distinctness)
Located in `theory/theorem_3_topological/`:
- `theorem_3_math.tex`: Complete mathematical proof using persistent homology and high-dimensional geometry
- `theorem_3_topological.ipynb`: Interactive Jupyter notebook with derivations and visualizations *(planned)*
- `README.md`: Theorem-specific documentation, assumptions, and implications

Each theorem folder includes:
- Formal mathematical statements and proofs
- Visualizations of key concepts *(planned)*
- Connections to empirical observations
- Detailed assumptions and boundary conditions

## Experiments

*The experimental framework is under active development. The following descriptions outline planned implementations.*

### 1. Lyapunov Exponents (`01_lyapunov/`) - *Under Development*
Will estimate maximal Lyapunov exponents for different architectures using the Benettin algorithm.

```bash
# Planned for future releases:
# python -m experiments.01_lyapunov.simulate --config experiments/01_lyapunov/config.yaml
```

### 2. Entropy Production (`02_entropy/`) - *Under Development*
Will compute entropy production rates during training using discrete-time stochastic thermodynamics.

```bash
# Planned for future releases:
# python -m experiments.02_entropy.simulate --config experiments/02_entropy/config.yaml
```

### 3. Topological Analysis (`03_topology/`) - *Under Development*
Will apply persistent homology to training trajectories to compute Wasserstein distances between persistence diagrams.

```bash
# Planned for future releases:
# python -m experiments.03_topology.simulate --config experiments/03_topology/config.yaml
```

Each experiment will include:
- Clean, modular Python code
- Configuration files for hyperparameters
- Visualization scripts
- Pre-computed results for verification

## Development Roadmap

**Version 0.0.1 (Current):** Project infrastructure and package setup  
**Version 0.1.0 (Planned):** Implementation of Theorem 1 (Chaotic divergence analysis)  
**Version 0.2.0 (Planned):** Implementation of Theorem 2 (Thermodynamic irreversibility)  
**Version 0.3.0 (Planned):** Implementation of Theorem 3 (Topological distinctness)  
**Version 1.0.0 (Planned):** Complete implementation with all experiments and documentation

## Citation

If you use this work, please cite:

```bibtex
@article{ghiassian2026uniqueness,
  title={Uniqueness in Deep Neural Networks: The Inevitable Singularity of Learning Trajectories},
  author={Ghiassian, Haamed},
  journal={Zenodo},
  year={2026},
  doi={10.5281/zenodo.18433336},
  url={https://doi.org/10.5281/zenodo.18433336}
}
```

## License

MIT License. See LICENSE file for details.

## Contact

For questions or discussions, please open an issue on GitHub or contact the author directly.
```
haamedghiasian@gmail.com
```
