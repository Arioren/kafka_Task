from app.db.models import Base
import sqlalchemy as sa

class Explosive(Base):
    __tablename__ = 'suspicious_explosive_content'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    sentence = sa.Column(sa.String)
    person_id = sa.Column(sa.Integer, sa.ForeignKey('person.id'))

    person = sa.relationship('Person', back_populates='sentences_explosive')