from enum import Enum
import numpy as np


class EuropeanOption:
    def __init__(self, strike_price: float, expiry: float):
        self.strike_price = strike_price
        self.expiry = expiry

    def payoff(self, path: np.ndarray) -> np.ndarray:
        raise NotImplementedError(f"Payoff needs to be implemented in child classes")


class EuropeanCallOption(EuropeanOption):
    def payoff(self, path: np.ndarray) -> np.ndarray:
        return np.maximum(0.0, path.loc[self.expiry] - self.strike_price)


if __name__ == "__main__":
    pass
