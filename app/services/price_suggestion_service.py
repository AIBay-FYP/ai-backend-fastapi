# # app/services/price_suggestion_service.py
# from app.database import listings_collection

# async def suggest_price(title: str, category: str, location: str, is_fixed: bool):
#     """
#     Suggests price using lightweight algorithm based on average demand score
#     and basic title/category keywords.
#     """
#     # Find similar listings from MongoDB to calculate average demand & price
#     query = {"Category": category}
#     similar_listings_cursor = listings_collection.find(query).limit(20)

#     total_demand = 0
#     count = 0
#     avg_price = 0

#     async for listing in similar_listings_cursor:
#         demand = listing.get("DemandScore", 1)
#         total_demand += demand
#         count += 1
#         price = listing.get("FixedPrice") or listing.get("MinPrice", 0)
#         avg_price += price

#     # Avoid division by zero
#     avg_demand = total_demand / count if count > 0 else 1
#     avg_price = avg_price / count if count > 0 else 100

#     # Score based on demand and keywords
#     score = avg_demand * 0.5 + avg_price * 0.5

#     # Add a small bonus if title has premium keyword
#     if "premium" in title.lower() or "latest" in title.lower():
#         score *= 1.1

#     # Decide based on is_fixed
#     if is_fixed:
#         fixed_price = round(score, 2)
#         return {"FixedPrice": fixed_price}
#     else:
#         min_price = round(score * 0.8, 2)
#         max_price = round(score * 1.2, 2)
#         return {"MinPrice": min_price, "MaxPrice": max_price}
