import time
from kafka.admin import KafkaAdminClient, NewTopic
from producer import IOTKafkaProducer
from fetcher import IOTFetcher
from config import KAFKA_BOOTSTRAP, KAFKA_TOPIC, SRC_URL

def check_topic(bootstrap_servers, topic_name, num_partitions=1, replication_factor=1):
    admin = KafkaAdminClient(bootstrap_servers=bootstrap_servers, client_id="iot_admin")
    existing_topics = admin.list_topics()

    if topic_name not in existing_topics:
        print(f"Topic: '{topic_name}' does not exist. Creating topic...")
        try:
            topic = NewTopic(
                name=topic_name,
                num_partitions=num_partitions,
                replication_factor=replication_factor
            )
            admin.create_topics([topic])
        except Exception as e:
            print(f"[check_topic] Error creating topic: {e}")
    else:
        print(f"Topic: '{topic_name}' already exists.")

    admin.close()

def main():
    check_topic(KAFKA_BOOTSTRAP, KAFKA_TOPIC)

    producer = IOTKafkaProducer(KAFKA_BOOTSTRAP, KAFKA_TOPIC)

    fetcher = IOTFetcher(
        url = SRC_URL,
        interval = 5,
        callback = lambda data: producer.publish(data)
    )

    fetcher.start()
    print(f"[driver_fetch.py] Fetcher started. Press CTRL+C to stop...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[Driver] Stopping gracefully...")
        fetcher.stop()
        fetcher.join()
        producer.close()
        print("\nFetcher stopped...")

if __name__ == "__main__":
    main()