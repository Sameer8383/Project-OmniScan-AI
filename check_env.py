import sys
import torch
import numpy as np
import pandas as pd
import pydicom
import sklearn

def verify_environment():
    print("=" * 50)
    print("PROJECT OMNISCAN AI: ENVIRONMENT VERIFICATION")
    print("=" * 50)
    print(f"Python Version: {sys.version.split()[0]}")
    print(f"NumPy Version: {np.__version__}")
    print(f"Pandas Version: {pd.__version__}")
    print(f"Scikit-Learn Version: {sklearn.__version__}")
    print(f"PyDicom Version: {pydicom.__version__}")
    print(f"PyTorch Version: {torch.__version__}")
    print(f"CUDA Available (GPU): {torch.cuda.is_available()}")
    print("=" * 50)
    print("Status: Environment successfully configured!")

if __name__ == "__main__":
    verify_environment()