# Real-Time Fraud Detection Pipeline

## 🚧 Project Status: In Development
*Note: This project is still being built. Features and components may be subject to change.*

## 📌 Project Overview
This project implements a real-time fraud detection pipeline using Apache Kafka, Apache Spark Streaming, Apache Airflow, and cloud data warehouses such as AWS Redshift or Snowflake. The goal is to detect fraudulent transactions in real-time by ingesting and processing streaming data efficiently.

## 🏗 Architecture Overview
The data pipeline follows this flow:
1. **Kafka Producer** generates and streams synthetic transaction data.
2. **Airflow DAGs** orchestrate the pipeline, managing data flow between components.
3. **Spark Structured Streaming** processes and detects fraudulent transactions.
4. **Processed data is stored** in Redshift/Snowflake for analysis.
5. **SQL queries** analyze and flag suspicious transactions.

![Architecture Diagram](docs/architecture_diagram.png)

## 📂 Folder Structure
```
real-time-fraud-detection/
├── dags/                          # Airflow DAGs for orchestration
│   ├── transaction_pipeline.py    # DAG to run end-to-end fraud detection pipeline
│   ├── kafka_to_s3_dag.py         # DAG to stream Kafka data to S3
│   ├── spark_processing_dag.py    # DAG to process streaming data with Spark
│   ├── redshift_loader.py         # DAG to load processed data into Redshift
│
├── kafka/                         # Kafka setup and producers
│   ├── transaction_producer.py    # Python script to produce transactions to Kafka
│   ├── kafka_docker_setup.sh      # Script to set up Kafka in Docker
│
├── spark/                         # Spark Streaming scripts
│   ├── fraud_detection.py         # Spark job to process streaming data
│   ├── spark_submit.sh            # Script to submit Spark jobs
│
├── infrastructure/                 # Terraform or CloudFormation scripts
│   ├── terraform_kafka.tf         # Infrastructure as Code (Kafka setup)
│   ├── terraform_redshift.tf      # Infra setup for Redshift/Snowflake
│   ├── airflow_docker_compose.yml # Airflow setup in Docker
│
├── sql/                           # SQL scripts for database setup & queries
│   ├── create_redshift_tables.sql # SQL to create Redshift fraud tables
│   ├── fraud_queries.sql          # SQL queries for fraud analysis
│
├── config/                        # Configuration files
│   ├── kafka_config.json          # Kafka connection settings
│   ├── redshift_config.json       # Redshift/Snowflake credentials
│   ├── airflow_config.py          # Airflow environment variables
│
├── notebooks/                     # Jupyter Notebooks for testing
│   ├── exploratory_analysis.ipynb # Data exploration on transactions
│
├── tests/                         # Unit and integration tests
│   ├── test_kafka_producer.py     # Unit test for Kafka producer
│   ├── test_spark_processing.py   # Unit test for Spark transformations
│   ├── test_redshift_loader.py    # Unit test for data loading
│
├── datasets/                      # Sample data for testing
│   ├── transactions_sample.csv    # Sample transaction dataset
│
├── docs/                          # Documentation
│   ├── architecture_diagram.png   # Diagram of data pipeline architecture
│   ├── pipeline_overview.md       # High-level explanation of the pipeline
│
├── README.md                      # Project documentation
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Docker containerization setup
├── .gitignore                      # Ignore unnecessary files
```

## 🚀 Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/real-time-fraud-detection.git
cd real-time-fraud-detection
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Start Kafka (Docker-based setup)
```bash
cd kafka
bash kafka_docker_setup.sh
```

### 4️⃣ Start Airflow
```bash
cd infrastructure
docker-compose -f airflow_docker_compose.yml up -d
```

### 5️⃣ Submit Spark Job
```bash
cd spark
bash spark_submit.sh
```

## 📌 Running the Pipeline
1. **Ensure Kafka is running.**
2. **Start Airflow and trigger DAGs.**
3. **Run Spark job for real-time fraud detection.**
4. **Load processed data into Redshift/Snowflake.**
5. **Analyze fraud trends using SQL queries.**

## ✅ Next Steps
1️⃣ Implement Machine Learning models for fraud detection.
2️⃣ Deploy the system on AWS/GCP using Kubernetes.
3️⃣ Optimize performance by tuning Spark and Redshift queries.

## 📌 Contribution
If you'd like to contribute, feel free to open an issue or submit a pull request! 🚀

