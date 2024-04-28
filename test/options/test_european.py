from pypricer.options import european
import pytest
import numpy as np
import pandas as pd


class TestEuropeanCallOption:

    @pytest.fixture
    def call_option(self):
        return european.EuropeanCallOption(strike_price=100.0, expiry=1.0)

    @pytest.mark.parametrize(
        "trajectory, expected_payoff",
        [
            ([99.0, 105.0], [5.0]),
            ([99.0, 100.0], [0.0]),
            ([99.0, 95.0], [0.0]),
            ([[99.0, 99.0], [105.0, 95.0]], [5.0, 0.0]),
        ],
        ids=[
            "In the money",
            "At the money",
            "Out of the money",
            "Multiple trajectories",
        ],
    )
    def test_payoff(
        self,
        call_option: european.EuropeanCallOption,
        trajectory: np.ndarray,
        expected_payoff: np.ndarray,
    ):
        trajectory = pd.DataFrame(np.array(trajectory), index=[0.9, 1.0])
        payoff = call_option.payoff(path=trajectory)
        np.testing.assert_allclose(payoff.values, np.array(expected_payoff))


if __name__ == "__main__":
    pass
