from typing import List, Optional
from pydantic import BaseModel


class Media(BaseModel):
    BibNum: int
    Title: str
    Author: str
    ISBN: Optional[str]
    PublicationYear: int
    Publisher: str
    Subjects: str
    ItemType: str
    ItemCount: int

    class Config:
        orm_mode = True


class MediaType(BaseModel):
    Code: str
    CodeType: str
    Description: str
    FormatGroup: str
    FormatSubgroup: Optional[str]
    CategoryGroup: Optional[str]
    CategorySubgroup: Optional[str]

    class Config:
        orm_mode = True


class CheckoutData(BaseModel):
    id: int
    BibNumber: int
    ItemBarcode: int
    ItemType: str
    CallNumber: str
    CheckoutDateTime: str

    class Config:
        orm_mode = True


class MediaResponse(BaseModel):
    count: int
    offset: int
    limit: int
    results: List[Media]


class MediaDetailResponse(BaseModel):
    source: Media
    source_type: MediaType
    checkout: List[CheckoutData]
