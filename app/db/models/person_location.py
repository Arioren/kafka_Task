from app.db.models import Base
import sqlalchemy as sa

class Location(Base):
    __tablename__ = 'location'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    latitude = sa.Column(sa.Float)
    longitude = sa.Column(sa.Float)
    city = sa.Column(sa.String)
    country = sa.Column(sa.String)

    person = sa.relationship('Person', back_populates='location')

