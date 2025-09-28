from kafka import KafkaConsumer
import json

# Kafka Consumer
consumer = KafkaConsumer(
    'driver-location',              # topic name (same as producer)
    bootstrap_servers=['localhost:29092'],  # external listener for Windows
    auto_offset_reset='earliest',   # read from beginning if no offsets yet
    enable_auto_commit=True,
    group_id='test-group',          # consumer group ID
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Listening for messages...")

for message in consumer:
    print(f"Received: {message.value}")
