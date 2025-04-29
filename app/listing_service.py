from app.database import listings_collection
from typing import Optional, List
from bson.objectid import ObjectId
from app.utils import serialize_mongo_document
from fastapi import HTTPException

async def search_listings(
    query: Optional[str] = None,
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    location: Optional[str] = None,
):
    filter_query = {}

    if query:
        filter_query["$or"] = [
            {"Title": {"$regex": query, "$options": "i"}},
            {"Description": {"$regex": query, "$options": "i"}},
            {"Keywords": {"$in": query.split(" ")}}
        ]

    if category:
        filter_query["Category"] = category

    if min_price and max_price:
        filter_query["$or"] = [
            {"FixedPrice": {"$gte": min_price, "$lte": max_price}},
            {"MinPrice": {"$gte": min_price}, "MaxPrice": {"$lte": max_price}},
        ]
    elif min_price:
        filter_query["$or"] = [
            {"FixedPrice": {"$gte": min_price}},
            {"MinPrice": {"$gte": min_price}},
        ]
    elif max_price:
        filter_query["$or"] = [
            {"FixedPrice": {"$lte": max_price}},
            {"MaxPrice": {"$lte": max_price}},
        ]

    if location:
        filter_query["Location"] = {"$regex": location, "$options": "i"}

    listings_cursor = listings_collection.find(filter_query)
    listings = []
    try:
        async for listing in listings_cursor:
            listing["_id"] = str(listing["_id"])
            listings.append(serialize_mongo_document(listing))
    except Exception as e:
        print("MongoDB query failed:", str(e))
        raise HTTPException(status_code=500, detail="Database query error")

    return listings