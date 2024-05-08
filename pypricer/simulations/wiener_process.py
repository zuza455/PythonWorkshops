import numpy as np
import pandas as pd


def generate_wiener_process(
    n_paths: int, n_steps: int, dt: float, sigma: float, mu: float
) -> pd.DataFrame:
    """Generate paths of the Wiener Process.

    Args:
        n_paths (int): Number of paths to generate.
        n_steps (int): Number of steps in each path.
        dt (float): Time step size.
        sigma (float): Volatility parameter (standard deviation of increments).
        mu (float): Drift parameter (mean rate of change per unit time).

    Returns:
        pd.DataFrame: Data of shape (n_paths, n_steps + 1) containing the Wiener process paths.
            Each row represents a different path, and each column represents a time step.
            The first row is the initial value (usually zero for Wiener processes).
    """
    paths = np.zeros((n_paths, n_steps + 1))
    t = np.linspace(0.0, dt * (n_steps + 1), n_steps + 1)
    for i in range(n_paths):
        for j in range(1, n_steps + 1):
            dW = np.random.normal(loc=mu * dt, scale=sigma * np.sqrt(dt))
            paths[i, j] = paths[i, j - 1] + dW

    paths_df = pd.DataFrame(paths.T, index=t)
    return paths_df


if __name__ == "__main__":
    pass
