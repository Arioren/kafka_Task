import json

from kafka import KafkaConsumer


def consume_emails_by_topic(topic: str):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='earliest'
    )
    for message in consumer:
        # member_collection.insert_one(message.value)
        print(f"Received: {message.key}: {message.value} \n from topic: {topic}")
