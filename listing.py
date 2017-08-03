import sqlalchemy
import sqlalchemy.ext.declarative

Base = sqlalchemy.ext.declarative.declarative_base()


class Listing(Base):
    listing_id = sqlalchemy.Column(sqlalchemy.Integer)
    last_update = sqlalchemy.Column(sqlalchemy.DateTime)
    city = sqlalchemy.Column(sqlalchemy.String(length=64))
