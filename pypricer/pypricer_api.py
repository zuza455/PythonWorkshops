from fastapi import FastAPI
import uvicorn
from pypricer.options import european
from pypricer.simulations import wiener_process

app = FastAPI()


@app.get("/price/european_call", tags=["Bachelier model"])
async def price_european_call(
    strike_price: float,
    expiry: float,
    n_paths: int,
    n_steps: int,
    dt: float,
    sigma: float,
    mu: float,
    rfr: float,
):
    """Calculate the price of a European call option using the Bachelier model.

    Args:
        strike_price (float): The strike price of the option.
        expiry (float): Time to expiration in years.
        n_paths (int): Number of simulated asset price paths.
        n_steps (int): Number of time steps in each path.
        dt (float): Time increment for each step in the simulation.
        sigma (float): Volatility of the asset price.
        mu (float): Drift of the asset price process.
        rfr (float): Risk-free rate.

    Returns:
        dict: A dictionary containing the calculated option price.
    """
    option = european.EuropeanCallOption(strike_price=strike_price, expiry=expiry)
    paths = wiener_process.generate_wiener_process(
        n_paths=n_paths, n_steps=n_steps, dt=dt, sigma=sigma, mu=mu
    )
    price = option.price(paths, rfr=rfr)
    return {"Price": price}


if __name__ == "__main__":
    uvicorn.run("pypricer_api:app", host="localhost", port=8080, reload=True)
