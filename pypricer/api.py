from fastapi import FastAPI
import uvicorn
from pypricer.options import european
from pypricer.simulations import wiener_process

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Go to /docs for the OpenAPI"}


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
    option = european.EuropeanCallOption(strike_price=strike_price, expiry=expiry)
    paths = wiener_process.generate_wiener_process(
        n_paths=n_paths, n_steps=n_steps, dt=dt, sigma=sigma, mu=mu
    )
    price = option.price(paths, rfr=rfr)
    return {"Price": price}


if __name__ == "__main__":
    uvicorn.run("api:app", host="localhost", port=8080, reload=True)
