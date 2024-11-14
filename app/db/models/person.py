from app.db.models import Base
import sqlalchemy as sa

class Person(Base):
    __tablename__ = 'person'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    email = sa.Column(sa.String)
    username = sa.Column(sa.String)
    ip_address = sa.Column(sa.String)
    created_at = sa.Column(sa.DateTime())

    location_id = sa.Column(sa.Integer, sa.ForeignKey('location.id'))
    device_info_id = sa.Column(sa.Integer, sa.ForeignKey('device_info.id'))

    device_info = sa.relationship('DeviceInfo', back_populates='person')
    location = sa.relationship('Location', back_populates='person')
    sentences_hostage = sa.relationship('Hostage', back_populates='person')
    sentences_explosive = sa.relationship('Explosive', back_populates='person')

