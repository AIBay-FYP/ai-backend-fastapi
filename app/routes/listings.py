from fastapi import APIRouter, Query
from typing import Optional
from app.listing_service import search_listings

router = APIRouter(
    prefix="/listings",
    tags=["Listings"]
)

@router.get("/search")
async def search(
    query: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    minPrice: Optional[float] = Query(None),
    maxPrice: Optional[float] = Query(None),
    location: Optional[str] = Query(None),
):
    listings = await search_listings(query, category, minPrice, maxPrice, location)
    return {"success": True, "data": listings}