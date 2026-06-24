"""Working NumPy example — run this file.

Run with:
    /workspaces/bootcamp-062026/.venv/bin/python day7/numpy_example.py
"""

import numpy as np


def main() -> None:
    print("NumPy examples:\n")

    # 1D arrays and basic ops
    a = np.array([1, 2, 3, 4])
    b = np.array([5, 6, 7, 8])
    print("a:", a)
    print("b:", b)
    print("a + b:", a + b)
    print("dot(a, b):", np.dot(a, b))

    # 2D arrays (matrices)
    mat = np.arange(1, 10).reshape(3, 3)
    print("\nmat:\n", mat)
    print("mat.T:\n", mat.T)
    print("mat @ mat (matrix multiply):\n", mat @ mat)
    print("mean, std:", mat.mean(), mat.std())

    # Random numbers via new Generator API
    rng = np.random.default_rng(0)
    samples = rng.normal(loc=0.0, scale=1.0, size=5)
    print("\nRandom samples:", samples)

    # Broadcasting example
    added = mat + np.array([10, 20, 30])
    print("\nBroadcasted add:\n", added)


if __name__ == "__main__":
    main()
