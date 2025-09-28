from kafka import KafkaProducer
import json
import time
import random

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:29092'],  # use EXTERNAL listener for Windows host
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize data to JSON
)

def send_location_updates(driver_id):
    while True:
        # Simulating random GPS coordinates (latitude, longitude)
        location = {
            "driver_id": driver_id,
            "latitude": round(random.uniform(40.0, 41.0), 6),
            "longitude": round(random.uniform(-74.0, -73.0), 6),
            "timestamp": time.time()
        }
        # Send location data to Kafka
        producer.send('driver-location', location)
        print(f"Sent: {location}")
        time.sleep(5)  # Sleep for 5 seconds to simulate real-time updates

# Start sending updates for driver_id = 101
send_location_updates(driver_id=101)
