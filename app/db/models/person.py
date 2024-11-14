from app.db.models import Base
import sqlalchemy as sa
import sqlalchemy.orm as orm

class Person(Base):
    __tablename__ = 'person'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    email = sa.Column(sa.String)
    username = sa.Column(sa.String)
    ip_address = sa.Column(sa.String)
    created_at = sa.Column(sa.String)

    location_id = sa.Column(sa.Integer, sa.ForeignKey('location.id'))
    device_info_id = sa.Column(sa.Integer, sa.ForeignKey('device_info.id'))

    device_info = orm.relationship('DeviceInfo', back_populates='person')
    location = orm.relationship('Location', back_populates='person')
    sentences_hostage = orm.relationship('Hostage', back_populates='person')
    sentences_explosive = orm.relationship('Explosive', back_populates='person')

