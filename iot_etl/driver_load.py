from config import KAFKA_BOOTSTRAP, KAFKA_TOPIC, MYSQL_CONFIG
from db_writer import MySQLWriter
from consumer import IOTKafkaConsumerDBIngestor
from utils import transform_iot_data

def main():
    db_writer = MySQLWriter(MYSQL_CONFIG)

    consumer = IOTKafkaConsumerDBIngestor(
        bootstrap_servers=KAFKA_BOOTSTRAP,
        topic=KAFKA_TOPIC
    )

    try:
        print("[driver_load.py] Consumer started. Press Ctrl+C to stop...")
        for iot_data in consumer.consume():
            iot_data = transform_iot_data(iot_data)
            db_writer.write(iot_data)
    except KeyboardInterrupt:
        print("\nConsumer stopping...")
    finally:
        consumer.close()
        print("Consumer stopped...")

if __name__ == "__main__":
    main()