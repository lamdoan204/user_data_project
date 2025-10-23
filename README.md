#  User Data Project

This project implements a **real-time user data processing pipeline** using modern data engineering tools.  
The system ingests, processes, and stores user information in a scalable, reliable, and containerized environment.

---

## 📊 System Architecture

The overall architecture follows a **data streaming pipeline** model.

![Architecture Diagram](./architecture.jpg)

### 🔹 Workflow Overview
1. **Data Ingestion**
   - Raw user data is fetched from external APIs 
   - The data is published to a Kafka topic for decoupled streaming.

2. **Data Streaming**
   - Kafka/Redpanda brokers act as the central event bus for the system.
   - Producers send events to topics while consumers (Spark, Airflow tasks) process them.

3. **Data Processing**
   - **Apache Spark** performs distributed transformations, cleaning, and enrichment.
   - Batch or streaming jobs can be orchestrated by **Apache Airflow** DAGs.

4. **Data Storage**
   - Processed data is stored in a persistent database (PostgreSQL).
   - This layer supports analytics and reporting.

5. **Orchestration & Monitoring**
   - Airflow handles workflow scheduling and dependency management.
   - Logs and metrics are available through the Dockerized environment.
---
---

## 🧱 Key Features

- Setting up a data pipeline with **Apache Airflow**
- Real-time data streaming with **Apache Kafka** (or **Redpanda**)
- Data processing techniques with **Apache Spark**
- Data storage solutions with **PostgreSQL**
- Containerizing your entire data engineering setup with **Docker**

---

## 🧰 Tools & Technologies

| Tool | Purpose |
|------|----------|
| **Docker** | Containerizes all components for consistent environment setup |
| **Kafka** | Handles real-time streaming of messages between producers and consumers |
| **Redpanda** | A modern, Kafka-compatible streaming platform with lower latency |
| **Apache Airflow** | Orchestrates, schedules, and monitors data processing pipelines |
| **Apache Spark** | Performs distributed data processing and analytics |
| **PostgreSQL** | Stores processed and cleaned data for downstream use |

---

