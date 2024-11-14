import json
from kafka import KafkaProducer

def produce_email(topic: str, email: dict):
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    producer.send(
        topic=f'messages.{topic}',
        value=email,
        key=email['email'].encode('utf-8')
    )
    producer.flush()
    print(f"Message sent successfully: {email}\n from topic:{topic}")