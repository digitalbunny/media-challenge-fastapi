from typing import Dict, Union, Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm.exc import NoResultFound
import schema
import db

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return {"message": "Hello from Fast API"}


@app.get("/media", response_model=schema.MediaResponse)
def media(offset: Optional[int] = 0, limit: Optional[int] = 20):
    results = db.session.query(db.Media).offset(offset).limit(limit).all()
    count = db.session.query(db.Media).count()
    return {
        "count": count - (offset + limit) if count - (offset + limit) >= 0 else 0,
        "offset": offset,
        "limit": limit,
        "results": results
    }


@app.get("/media/{bib_num}",  response_model=Union[schema.MediaDetailResponse, Dict[str, str]])
async def detail(bib_num: int):
    try:
        source, source_type = db.session.\
            query(db.Media, db.MediaType).\
            join(db.MediaType, db.Media.ItemType == db.MediaType.Code).\
            filter(db.Media.BibNum == bib_num).first()
    except TypeError:
        return {"message": "Item not found"}
    else:
        checkout = db.session.query(db.CheckoutData).filter(db.CheckoutData.BibNumber == source.BibNum).all()
        return {
            "source": source,
            "source_type": source_type,
            "checkout": checkout
        }