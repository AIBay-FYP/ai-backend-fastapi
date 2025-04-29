# database.py
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://aibaysite:Icvx1v49zs7LnfMb@aibay.alnl0.mongodb.net/")
DATABASE_NAME = os.getenv("DATABASE_NAME", "servicemarketplace")  

try:
    client = AsyncIOMotorClient(MONGO_URI)
    db = client[DATABASE_NAME]
    listings_collection = db["listings"]
    print("MongoDB Connected")
except Exception as e:
    print("MongoDB connection error:", e)
    raise e  # Fail fast if can't connect
