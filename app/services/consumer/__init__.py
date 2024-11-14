import json

from kafka import KafkaConsumer
from app.repository.sql_repo import insert_email_into_sql


def consume_emails_by_topic(topic: str):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='earliest'
    )
    for message in consumer:
        if topic == 'messages.hostage' or topic == 'messages.explosive':
            insert_email_into_sql(message.value, topic)
        print(f"Received: {message.key}: {message.value} \n from topic: {topic}")
