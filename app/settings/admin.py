from kafka import KafkaAdminClient
from kafka.admin import NewTopic
topics = [
   {"name": "messages.all", "partitions": 3, "replication": 1},
   {"name": "messages.hostage", "partitions": 3, "replication": 1},
   {"name": "messages.explosive", "partitions": 3, "replication": 1},
]


def init_topics():
   admin_client = KafkaAdminClient(bootstrap_servers='localhost:9092')
   topic_list = [
       NewTopic(
               name=topic["name"],
               num_partitions=topic["partitions"],
               replication_factor=topic["replication"]
           ) for topic in topics
   ]
   try:
       admin_client.create_topics(new_topics=topic_list, validate_only=False)
       print("Topics created successfully!")
   except Exception as e:
       print(f"Error creating topics: {e}")
   finally:
       admin_client.close()

