from app.db.database import all_emails
from app.services.producer.produce_emails import produce_email


def new_email(body: dict):
    res = all_emails.insert_one(body)
    produce_email('all', body)

    type = type_of_email(body)
    if type == 'hostage':
        produce_email(type, body)
    if type == 'explosive':
        produce_email(type, body)
    return res



def type_of_email(body: dict)->str:
    for i, sentence in enumerate(body['sentences']):
        if 'hostage' in sentence:
            body['sentences'] = [sentence].append(body['sentences'][i + 1:])
            return 'hostage'
        elif 'explosive' in sentence:
            body['sentences'] = [sentence].append(body['sentences'][i + 1:])
            return 'explosive'
    return 'all'



