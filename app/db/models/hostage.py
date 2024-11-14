from app.db.models import Base
import sqlalchemy as sa
import sqlalchemy.orm as orm

class Hostage(Base):
    __tablename__ = 'suspicious_hostage_content'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    sentence = sa.Column(sa.String)
    person_id = sa.Column(sa.Integer, sa.ForeignKey('person.id'))

    person = orm.relationship('Person', back_populates='sentences_hostage')