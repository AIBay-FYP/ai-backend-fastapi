from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class FAQ(BaseModel):
    question: str
    answer: Optional[str] = ""

class Listing(BaseModel):
    ProviderID: str
    Title: str
    Description: str
    IsNegotiable: bool
    IsFixedPrice: bool
    Availability: bool
    Category: str
    Photos: List[str]
    DemandScore: Optional[float] = 0
    FAQs: Optional[List[FAQ]] = []
    ServiceType: str
    DateCreated: Optional[datetime] = None
    DatePosted: Optional[datetime] = None
    Location: str
    DaysAvailable: Optional[int]
    SecurityFee: Optional[float]
    CancellationFee: Optional[float]
    Keywords: Optional[List[str]] = []
    MaxPrice: Optional[float]
    MinPrice: Optional[float]
    FixedPrice: Optional[float] = 0
    RentalDays: Optional[int]
    Qunatity: Optional[int]
    Currency: Optional[str]
    Documents: Optional[List[str]] = []