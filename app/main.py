from fastapi import FastAPI
from routes import listings

app = FastAPI()

# Include the listing routes
app.include_router(listings.router)

@app.get("/")
def read_root():
    return {"message": "FastAPI Search API is up and running"}
