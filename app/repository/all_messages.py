from app.db.database import all_emails
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



