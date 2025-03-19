# **Airflow & Redshift Data Pipeline**

## **Project Overview**
This project demonstrates an **ETL pipeline using Apache Airflow and AWS Redshift**, designed to process and transform log data from S3 into a structured analytical format. The pipeline follows a **DAG (Directed Acyclic Graph) architecture**, orchestrating data extraction, loading, transformation, and validation.

### **Key Features**
- **Data Ingestion**: Extracts raw log data from **AWS S3** and stages it into **Amazon Redshift**.
- **Data Transformation**: Loads staging data into **fact and dimension tables**.
- **Automated Workflow**: Uses **Apache Airflow** to manage task dependencies and scheduling.
- **Data Quality Checks**: Ensures integrity using SQL-based **data validation tests**.
- **Scalability**: Supports large-scale **log data processing** in the cloud.

---

## **Technologies Used**
- **Apache Airflow** – DAG orchestration
- **Amazon Redshift** – Data warehouse
- **Amazon S3** – Storage for raw log files
- **Python** – ETL scripting and SQL execution
- **SQL** – Data transformations and integrity checks
- **AWS IAM** – Credential management

---

## **Project Structure**
```
├── dags/
│   ├── udac_dag.py  # Main Airflow DAG definition
├── plugins/
│   ├── helpers/
│   │   ├── sql_queries.py  # SQL queries for transformations
│   ├── operators/
│   │   ├── stage_redshift.py  # Loads data from S3 to Redshift
│   │   ├── load_fact.py  # Loads data into fact table
│   │   ├── load_dimension.py  # Loads data into dimension tables
│   │   ├── data_quality.py  # Performs data validation
├── README.md  # Project documentation
```

---

## **ETL Pipeline Workflow**

1. **Stage Events & Songs Data from S3 to Redshift**
   - Reads raw log and song data from **S3**.
   - Loads it into Redshift **staging tables**.

2. **Load Data into Fact Table**
   - Transforms staged data and inserts records into the **songplays fact table**.

3. **Load Data into Dimension Tables**
   - Populates **users, songs, artists, and time** dimension tables.
   - Uses `truncate-before-insert` strategy for idempotency.

4. **Run Data Quality Checks**
   - Ensures **no NULL values in primary keys**.
   - Confirms **row counts match expected values**.

---

## **Installation & Setup**
### **1. Clone the Repository**
```sh
git clone https://github.com/yourusername/airflow-redshift-etl.git
cd airflow-redshift-etl
```

### **2. Install Dependencies**
```sh
pip install apache-airflow
```

### **3. Configure Airflow & AWS**
- Set up **AWS credentials** in Airflow connections (`aws_credentials`).
- Configure **Redshift connection (`redshift`)** in Airflow.

### **4. Start Airflow Scheduler & Webserver**
```sh
airflow scheduler & airflow webserver -p 8080
```
Access the Airflow UI at: **`http://localhost:8080`**

### **5. Trigger the DAG**
In Airflow UI, **turn on** the `udac_dag` DAG and trigger execution.

---

## **SQL Queries Used**
### **Fact Table (songplays)**
```sql
SELECT
    md5(events.sessionid || events.start_time) AS songplay_id,
    events.start_time,
    events.userid,
    events.level,
    songs.song_id,
    songs.artist_id,
    events.sessionid,
    events.location,
    events.useragent
FROM staging_events events
LEFT JOIN staging_songs songs
ON events.song = songs.title
AND events.artist = songs.artist_name;
```

### **Dimension Tables**
```sql
SELECT DISTINCT userid, firstname, lastname, gender, level
FROM staging_events
WHERE page='NextSong';
```

---

## **Future Enhancements**
✅ **Deploy on AWS MWAA (Managed Workflows for Apache Airflow)**
✅ **Integrate Airflow with AWS Lambda for event-driven processing**
✅ **Implement partitioning for Redshift tables for better query performance**
✅ **Add automated alerting via Slack or AWS SNS**

---

## **Contributions & Contact**
🔹 If you'd like to contribute, feel free to submit a **pull request**.
🔹 Questions? Reach out via GitHub issues or connect with me!