# IoT ETL Pipeline  

This project implements an **Extract-Transform-Load (ETL) pipeline** for IoT data using **Kafka** for streaming and **MySQL** for storage. It is designed to handle real-time ingestion of IoT device data, process it, and persist it into a relational database for further analytics.  

---

## 📌 Features
- **Data Ingestion** → Kafka producer fetches IoT data from external sources.  
- **Stream Processing** → Kafka consumer listens to topics in real time.  
- **Database Storage** → Processed data is written into MySQL.  
- **Configurable** → Centralized `config.py` for managing Kafka & DB settings.  
- **Modular Design** → Clean separation of producer, consumer, DB writer, and utilities.  

---

🛠️ Tech Stack

Python → Core ETL logic

Apache Kafka → Message broker

MySQL → Storage backend


📊 Use Cases

IoT device telemetry ingestion

Real-time monitoring dashboards

Data warehousing for analytics
