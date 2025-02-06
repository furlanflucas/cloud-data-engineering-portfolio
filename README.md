# Data-Pipelines-with-Airflow

This project builds an end-to-end data pipeline using Apache Airflow to load, transform, and validate data stored in Amazon S3 and Amazon Redshift. The pipeline processes JSON log and song data to populate a star-schema optimized for analytics.

---

## Table of Contents

- [Overview](#overview)
- [Datasets](#datasets)
- [Project Setup](#project-setup)
- [S3 Data Setup](#s3-data-setup)
- [Project Template Structure](#project-template-structure)
- [Airflow DAG Configuration](#airflow-dag-configuration)
- [DAG Default Parameters](#dag-default-parameters)
- [Task Dependencies](#task-dependencies)
- [Operators Overview](#operators-overview)
- [Stage Operator](#stage-operator)
- [Fact and Dimension Operators](#fact-and-dimension-operators)
- [Data Quality Operator](#data-quality-operator)
- [Getting Started](#getting-started)
- [Additional Notes](#additional-notes)

---

## Overview

This project demonstrates how to:
- Ingest JSON data from Amazon S3 into Amazon Redshift.
- Transform the data into a fact and dimension schema.
- Ensure data quality with a set of SQL-based tests.
- Manage task execution and dependencies using Apache Airflow.

---

## Datasets

The project uses two primary datasets hosted in Udacity's S3 bucket:

- **Log Data:** `s3://udacity-dend/log_data`
- **Song Data:** `s3://udacity-dend/song-data`

> **Tip:** It is recommended to copy the data from the Udacity bucket to your own S3 bucket in the same AWS Region where your Redshift cluster is located.

---

## Project Setup

### S3 Data Setup

Follow these steps to copy the data to your own S3 bucket:

1. **Create Your Own S3 Bucket**  
   Use the AWS CloudShell to create your bucket (replace `your-unique-bucket-name` with your desired bucket name):

   ```bash
   aws s3 mb s3://your-unique-bucket-name/
   ```

2. **Copy Data from Udacity's S3 Bucket to CloudShell Directory**

   ```bash
   aws s3 cp s3://udacity-dend/log-data/ ~/log-data/ --recursive
   aws s3 cp s3://udacity-dend/song-data/ ~/song-data/ --recursive
   aws s3 cp s3://udacity-dend/log_json_path.json ~/
   ```

3. **Upload the Data to Your Own S3 Bucket**

   ```bash
   aws s3 cp ~/log-data/ s3://your-unique-bucket-name/log-data/ --recursive
   aws s3 cp ~/song-data/ s3://your-unique-bucket-name/song-data/ --recursive
   aws s3 cp ~/log_json_path.json s3://your-unique-bucket-name/
   ```

4. **Verify the Upload**

   ```bash
   aws s3 ls s3://your-unique-bucket-name/log-data/
   aws s3 ls s3://your-unique-bucket-name/song-data/
   aws s3 ls s3://your-unique-bucket-name/log_json_path.json
   ```

### Project Template Structure

The provided project template includes the following components:

- **DAG Template:**  
  Contains all necessary imports, task templates, and placeholders for task dependencies.
  
- **Operators Folder:**  
  Contains operator templates that need to be implemented:
  - **Stage Operator:** Loads JSON files from S3 to Redshift.
  - **Fact Operator:** Loads fact table data into Redshift.
  - **Dimension Operator:** Loads dimension table data into Redshift (typically using a truncate-insert pattern).
  - **Data Quality Operator:** Runs SQL-based data quality checks.

- **SQL Helper Class:**  
  Contains SQL transformation templates to support data operations.

> **Note:** Once the DAG is configured correctly, you should see it in the Airflow UI with a graph similar to the provided screenshots.

---

## Airflow DAG Configuration

### DAG Default Parameters

Configure the DAG with the following default parameters:

- **Dependencies on past runs:** Disabled (i.e., no dependencies on past runs)
- **Retries:** 3 attempts per task
- **Retry Delay:** 5 minutes between retries
- **Catchup:** Disabled
- **Email on Retry:** Disabled

### Task Dependencies

The pipeline consists of the following tasks, which should be configured with the dependencies outlined below:

1. **Begin_execution**
2. **Stage_events** and **Stage_songs**  
   _Both tasks start after Begin_execution._
3. **Load_songplays_fact_table**  
   _Starts after both staging tasks complete._
4. **Load_artist_dim_table**, **Load_song_dim_table**, **Load_time_dim_table**, **Load_user_dim_table**  
   _All four tasks run concurrently after the fact table is loaded._
5. **Run_data_quality_checks**  
   _Executes after all four dimension tasks have completed._
6. **Stop_execution**  
   _Runs after the data quality checks are successful._

The intended flow:

```
Begin_execution
      ├──> Stage_events
      └──> Stage_songs
                │
         [Both complete]
                │
         Load_songplays_fact_table
                │
         ┌──────┬──────┬──────┬──────┐
         │      │      │      │      │
 Load_artist_dim  Load_song_dim  Load_time_dim  Load_user_dim
         └──────┴──────┴──────┴──────┘
                │
     Run_data_quality_checks
                │
         Stop_execution
```

---

## Operators Overview

### Stage Operator

- **Purpose:**  
  Loads any JSON-formatted files from S3 into a staging table in Redshift.
- **Key Features:**
  - Accepts parameters to specify the S3 path and target Redshift table.
  - Utilizes a templated field to load timestamped files for dynamic file ingestion.

### Fact and Dimension Operators

- **Fact Operator:**
  - Loads data into the fact table using an append-only strategy.
- **Dimension Operator:**
  - Loads data into dimension tables, typically using a truncate-insert pattern.
- **Common Features:**
  - Leverage the SQL helper class for data transformations.
  - Accept input SQL queries and target table names to run transformations against Redshift.

### Data Quality Operator

- **Purpose:**  
  Runs SQL-based data quality tests against the tables in Redshift.
- **Functionality:**
  - Accepts one or more SQL queries along with expected results.
  - Compares the result of each query to the expected result.
  - Raises an exception if any test fails, triggering task retries and eventual failure if unresolved.

---

## Getting Started

1. **Download or Clone the Project Template:**
   - If using the Udacity workspace, the template will be preloaded.
   - Alternatively, clone the repository from GitHub as per the instructions in the provided README.

2. **Configure AWS Credentials:**
   - Ensure that your AWS credentials are set up for accessing S3 and Redshift.

3. **Update the DAG and Operator Code:**
   - Complete the DAG configuration by setting the default parameters and task dependencies as described.
   - Implement the logic in the operator templates (Stage, Fact, Dimension, and Data Quality).

4. **Deploy and Test in Airflow:**
   - Place your DAG file in the Airflow DAGs folder.
   - Start Airflow, access the UI, and verify that the DAG graph reflects the correct task dependencies.
   - Execute the DAG and review logs to ensure all tasks are implemented and working correctly.

5. **Submission:**
   - Once the DAG executes successfully, package your final solution as a zip file or submit via your forked GitHub repository as required.

---

## Additional Notes

- **Backfills and Dynamic Loading:**  
  The Stage Operator’s templated field allows loading files based on execution time, making it easy to run backfills for historical data.
  
- **Extensibility:**  
  The structure of the operators and DAG configuration makes it straightforward to extend this pipeline to handle additional datasets or transformations in the future.

- **Airflow UI:**  
  After deploying your DAG, click on the "Links" button at the bottom of the Udacity workspace to access the Airflow UI for monitoring and debugging.

---
