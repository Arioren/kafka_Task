from collections import Counter
from functools import reduce

from app.db.database import all_emails, session_maker
from app.db.models import Person
from app.services.producer.produce_emails import produce_email


def new_email(body: dict):
    all_emails.insert_one(body)
    body['_id'] = str(body['_id'])

    produce_email('all', body)

    topic = type_of_email(body)
    if topic == 'hostage':
        produce_email(topic, body)
    if topic == 'explosive':
        produce_email(topic, body)
    return body



def type_of_email(body: dict)->str:
    for i, sentence in enumerate(body['sentences']):
        if 'hostage' in sentence:
            new_list = [sentence] + list(body['sentences'][:i]) + list(body['sentences'][i + 1:])
            body['sentences'] = new_list
            return 'hostage'
        elif 'explosive' in sentence:
            new_list = [sentence] + list(body['sentences'][:i]) + list(body['sentences'][i + 1:])
            body['sentences'] = new_list
            return 'explosive'
    return 'all'


def get_person_by_email(email: str):
    with session_maker() as session:
        person = session.query(Person).filter(Person.email == email).first()
        return {'email': person.email,
            'username': person.username,
            'ip_address': person.ip_address,
            'created_at': person.created_at,
            'location':{
                'latitude': person.location.latitude,
                'longitude': person.location.longitude,
                'city': person.location.city,
                'country': person.location.country
            },
            'device_info':{
                'browser': person.device_info.browser,
                'os': person.device_info.os,
                'device_id': person.device_info.device_id
            },
            'sentences_hostage':[sentence.sentence for sentence in person.sentences_hostage],
            'sentences_explosive': [sentence.sentence for sentence in person.sentences_explosive]
            }


def get_most_common_word(email: str):
    with session_maker() as session:
        person = session.query(Person).filter(Person.email == email).first()
        all_sentences = [sentence.sentence for sentence in person.sentences_hostage] + [sentence.sentence for sentence in person.sentences_explosive]
        all_words = reduce(lambda x, y: x + y, map(lambda x: x.split(' '), all_sentences))
        words_rank = Counter(all_words).most_common()
        return words_rank[0][0]



