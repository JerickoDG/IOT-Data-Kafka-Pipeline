import json
from datetime import datetime as dt
from kafka import KafkaProducer
from kafka.errors import KafkaError


class IOTKafkaProducer:
    def __init__(self, bootstrap_servers, topic):
        self.topic = topic
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            retries=5
        )
        self.sent_timestamps = set()  # To track sent timestamps and avoid duplicates

    def publish(self, iot_data: dict):
        timestamp = iot_data.get("created_at")
        if timestamp is None:
            print("[IOTKafkaProducer] Missing 'created_at' in data, skipping publish.")
            return

        if timestamp in self.sent_timestamps:
            print(f"[IOTKafkaProducer] Duplicate timestamp {timestamp}, skipping publish.")
            return
        
        try:
            fut = self.producer.send(self.topic, iot_data)
            fut.get(timeout=10) # block until sent or error
            self.sent_timestamps.add(timestamp)  # To track sent timestamps and avoid duplicates
            print(f"[IOTKafkaProducer] produced {timestamp} at {dt.now().replace(microsecond=0)}")
        except KafkaError as e:
            print(f"[IOTKafkaProducer] Error publishing iot data at {dt.now().replace(microsecond=0)}: {e}")

    def close(self):
        self.producer.flush()
        self.producer.close()