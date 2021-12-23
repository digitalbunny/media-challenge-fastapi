from sqlalchemy import create_engine
from sqlalchemy.orm import Session, join
from sqlalchemy.ext.automap import automap_base

SQLALCHEMY_DATABASE_URL = "mysql://Zuno:ZunoInterview@zunolibrary.cv07g5ggoiyj.us-east-2.rds.amazonaws.com/library"

Base = automap_base()
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Reflect existing database tables
Base.prepare(engine, reflect=True)

# Create mapped classes matching database table names
Media = Base.classes.media
MediaType = Base.classes.media_type
CheckoutData = Base.classes.checkout_data

session = Session(engine)
