from symbol import lambdef_nocond

from app.db.database import session_maker
from app.db.models import Person, Location, DeviceInfo, Hostage, Explosive


def insert_email_into_sql(email: dict, topic: str):
    with session_maker() as session:
        location = Location(
            city=email['location']['city'],
            country=email['location']['country'],
            latitude=email['location']['latitude'],
            longitude=email['location']['longitude']
        )
        session.add(location)
        session.commit()
        session.refresh(location)

        device_info = DeviceInfo(
            browser=email['device_info']['browser'],
            os=email['device_info']['os'],
            device_id=email['device_info']['device_id']
        )
        session.add(device_info)
        session.commit()
        session.refresh(device_info)

        person = Person(
            email=email['email'],
            username=email['username'],
            ip_address=email['ip_address'],
            created_at=email['created_at'],
            location_id=location.id,
            device_info_id=device_info.id
        )
        session.add(person)
        session.commit()
        session.refresh(person)

        if topic == 'messages.hostage':
            for sentence in email['sentences']:
                session.add(Hostage(sentence=sentence, person_id=person.id))
        elif topic == 'messages.explosive':
            for sentence in email['sentences']:
                session.add(Explosive(sentence=sentence, person_id=person.id))

        session.commit()

