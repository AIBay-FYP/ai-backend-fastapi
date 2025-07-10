from fastapi import FastAPI
from app.routes import listings
from app.routes import price

app = FastAPI()

# Include the listing routes
app.include_router(listings.router)
app.include_router(price.router) 

@app.get("/")
def read_root():
    return {"message": "FastAPI Search API is up and running"}
