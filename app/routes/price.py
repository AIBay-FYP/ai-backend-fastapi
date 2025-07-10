# app/routes/price.py
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

router = APIRouter(
    prefix="/pricing",
    tags=["Pricing"]
)

class PriceSuggestionRequest(BaseModel):
    title: str
    category: str
    location: str
    is_fixed: bool

# Define the logic directly here
async def suggest_price(title: str, category: str, location: str, is_fixed: bool):
    # Example lightweight logic: set a base price based on category length etc.
    score = len(title) + len(category)  # trivial example
    if is_fixed:
        return {"FixedPrice": round(score * 10, 2)}
    else:
        return {"MinPrice": round(score * 8, 2), "MaxPrice": round(score * 12, 2)}

@router.post("/price-suggestion")
async def price_suggestion(request: PriceSuggestionRequest):
    suggestion = await suggest_price(
        title=request.title,
        category=request.category,
        location=request.location,
        is_fixed=request.is_fixed
    )
    return {"success": True, "data": suggestion}
