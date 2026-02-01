"""
Uniqueness in Deep Neural Networks
Official implementation of the paper "Uniqueness in Deep Neural Networks: 
The Inevitable Singularity of Learning Trajectories"

This is the initial release (version 0.0.1) for name reservation.
Full functionality will be available in future releases.

GitHub: https://github.com/HaAmedghiassian/uniq-nets
"""

__version__ = "0.0.1"
__author__ = "Haamed Ghiassian"
__email__ = "haamed.ghiassian@gmail.com"
__url__ = "https://github.com/HaAmedghiassian/uniq-nets"

# Modules will be imported here in future releases
# from .lyapunov import *
# from .entropy import *
# from .topology import *

def hello():
    """Welcome message for the initial release."""
    return f"uniq-nets v{__version__} - Under active development"

# Print welcome message when imported directly
if __name__ == "uniq_nets":
    print(f"✨ uniq-nets v{__version__}")
    print("📚 Research package for 'Uniqueness in Deep Neural Networks'")
    print("🚀 Under active development - Full release coming soon!")
    print("🔗 GitHub: https://github.com/HaAmedghiassian/uniq-nets")
    print("📧 Author: Haamed Ghiassian")
    print("---")
