import json
from datetime import datetime as dt
from kafka import KafkaConsumer
from kafka.errors import KafkaError


class IOTKafkaConsumerDBIngestor():
    def __init__(self, bootstrap_servers, topic, group_id="iot_group"):
        self.topic = topic
        self.consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=bootstrap_servers,
            group_id=group_id,
            value_deserializer=lambda v: json.loads(v.decode('utf-8'))
        )

    def consume(self):
        try:
            for message in self.consumer:
                yield message.value
        except KafkaError as e:
            print(f"[IOTKafkaConsumerDBIngestor] Error consuming iot data at {dt.now().replace(microsecond=0)}: {e}")
    
    def close(self):
        self.consumer.close()