import json

from flask import Flask
from kafka import KafkaConsumer

app = Flask(__name__)

def consume_emails_by_topic(topic: str):
    consumer = KafkaConsumer(
        'topic',
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='earliest'
    )
    for message in consumer:
        # member_collection.insert_one(message.value)
        print(f"Received: {message.key}: {message.value} \n from topic: {topic}")


if __name__ == '__main__':
    consume_emails_by_topic('messages.all')
    consume_emails_by_topic('messages.hostage')
    consume_emails_by_topic('messages.explosive')
    app.run()