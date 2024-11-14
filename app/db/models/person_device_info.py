from app.db.models import Base
import sqlalchemy as sa

class DeviceInfo(Base):
    __tablename__ = 'device_info'
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    browser = sa.Column(sa.String)
    os = sa.Column(sa.String)
    device_id = sa.Column(sa.String)

    person = sa.relationship('Person', back_populates='device_info')
