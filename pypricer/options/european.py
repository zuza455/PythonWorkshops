"""
Option Pricing Module

This module provides classes for pricing European options using different protocols.
"""

import numpy as np
import pandas as pd


class EuropeanOption:
    """Parent class for european options"""

    def __init__(self, strike_price: float, expiry: float):
        self.strike_price = strike_price
        self.expiry = expiry

    def payoff(self, path: pd.DataFrame) -> pd.DataFrame:
        """Abstract method"""
        raise NotImplementedError("Payoff needs to be implemented in child classes")

    def price(self, path: pd.DataFrame, rfr: float) -> float:
        """Abstract method"""
        raise NotImplementedError("Pricing needs to be implemented in child classes")


class EuropeanCallOption(EuropeanOption):
    """Child class implementing call option protocol"""

    def payoff(self, path: pd.DataFrame) -> np.ndarray:
        """Compute option payoff

        Args:
            path (pd.DataFrame): Dataset with asset price realizations.
                Columns are trajectories, rows is the time index.

        Returns:
            pd.DataFrame: Dataset with payoffs for each trajectory
        """
        return np.maximum(0.0, path.iloc[-1, :] - self.strike_price)

    def price(self, path: pd.DataFrame, rfr: float) -> np.ndarray:
        """Compute the price of the option using the Black-Scholes formula.

        Args:
            path (pd.DataFrame): DataFrame with asset price realizations.
                Columns represent different trajectories, rows represent time steps.
            rfr (float): Risk-free rate.

        Returns:
            np.ndarray: Array containing option prices for each trajectory.
        """
        return np.exp(-self.expiry * rfr) * self.payoff(path=path).mean()


if __name__ == "__main__":
    pass
