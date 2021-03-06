import sqlalchemy
import sqlalchemy.ext.declarative

Base = sqlalchemy.ext.declarative.declarative_base()


class Listing(Base):
    __tablename__ = 'listing'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    listing_id = sqlalchemy.Column(sqlalchemy.Integer)
    last_update = sqlalchemy.Column(sqlalchemy.TIMESTAMP(timezone=True))
    city = sqlalchemy.Column(sqlalchemy.String(length=64))
