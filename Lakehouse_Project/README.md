# STEDI Lakehouse Solution

## Project Overview

This project uses **AWS Glue**, **AWS S3**, **Python**, and **Spark** to build a Lakehouse solution that satisfies the requirements of the STEDI data scientists. The solution involves setting up landing, trusted, and curated zones, sanitizing data, and creating tables for machine learning.

---

## Workflow

Refer to the workflow and relationship diagrams provided in the project documentation for guidance. The key steps are outlined below.

---

# Steps for Setting Up and Processing Data

## 1. Setup S3 Buckets

### Create S3 Buckets
Create the following buckets for landing zones:
- `customer–bucket/`
- `accelerometer--bucket/`
- `step_trainer–bucket/`

### Copy the JSON Data into These Buckets
- **Place customer data** in `customer_landing_folder/`.
- **Place accelerometer data** in `accelerometer_landing_folder/`.
- **Place step trainer data** in `step_trainer_landing_folder/`.

---

## 2. Create Glue Tables from Landing Zone Data

### Use Glue Console to Create Tables
1. Go to **AWS Glue Console** → **Databases**.
2. Create a new database: `stedi`.
3. Use the **Crawler** to set up table creation for each dataset.

### Query Data with Athena
Validate table creation by querying each table:

- Query for `customer_landing_folder`:
  ```sql
  SELECT COUNT(*) FROM customer_landing_folder;
  ```
  **Expected Result:** 956 rows.

- Query for `accelerometer_landing_folder`:
  ```sql
  SELECT COUNT(*) FROM accelerometer_landing_folder;
  ```
  **Expected Result:** 81,273 rows.

- Query for `step_trainer_landing_folder`:
  ```sql
  SELECT COUNT(*) FROM step_trainer_landing_folder;
  ```
  **Expected Result:** 28,680 rows.

Take screenshots of the query results for documentation.

---

## S3 Bucket Paths
- `s3://accelerometer--bucket/accelerometer_landing_folder/`
- `s3://customer--bucket/customer_landing_folder/`
- `s3://step-trainer--bucket/step_trainer_landing_folder/`
---

### 4. **Sanitize Data for the Trusted Zone**

Create two AWS Glue jobs:
1. **Sanitize `customer_landing` Data:**
   - Filter for customers who agreed to share their data.
   - Output: `customer_trusted` Glue Table.
2. **Sanitize `accelerometer_landing` Data:**
   - Filter accelerometer records for customers who agreed to share their data.
   - Output: `accelerometer_trusted` Glue Table.

---

### 5. **Query Trusted Zone Tables**
- Use **Athena** to query the `customer_trusted` and `accelerometer_trusted` tables:
  - Query: `SELECT * FROM stedi.customer_trusted LIMIT 10;`
  - Query: `SELECT * FROM stedi.accelerometer_trusted LIMIT 10;`
- Take screenshots of the results and save them as:
  - `customer_trusted.png`
  - `accelerometer_trusted.png`

---

### 6. **Resolve Serial Number Issue**
- Fix the serial number issue in `customer_landing`:
  - Match customer records to accelerometer records.
  - Create a new table: `customers_curated`.

---

### 7. **Glue Studio Jobs for Curated Zone**

Create two Glue Studio jobs:
1. **Process Step Trainer IoT Data:**
   - Filter `step_trainer_landing` data for customers with accelerometer data.
   - Output: `step_trainer_trusted` Glue Table.
2. **Create Machine Learning Curated Table:**
   - Join `step_trainer_trusted` with `accelerometer_trusted` on `timestamp`.
   - Aggregate data for machine learning use.
   - Output: `machine_learning_curated` Glue Table.

---

### 8. **Verify Row Counts**
After each stage, verify the row counts in the produced tables. Expected row counts:

| Zone       | Table                     | Row Count |
|------------|---------------------------|-----------|
| Landing    | `customer_landing`        | 956       |
| Landing    | `accelerometer_landing`   | 81,273    |
| Landing    | `step_trainer_landing`    | 28,680    |
| Trusted    | `customer_trusted`        | 482       |
| Trusted    | `accelerometer_trusted`   | 40,981    |
| Trusted    | `step_trainer_trusted`    | 14,460    |
| Curated    | `customers_curated`       | 482       |
| Curated    | `machine_learning_curated` | 43,681    |

---

### 9. **Final Documentation**
- Include the following:
  - Screenshots for queries and row counts.
  - SQL scripts for creating tables.
  - Glue scripts for sanitization and processing.
- Upload all scripts and screenshots to the Git repository.

---

## Tools Used
- **AWS Glue**
- **AWS S3**
- **Apache Spark**
- **Python**
- **Amazon Athena**

---

## Author
This project was created as part of a data engineering workflow to build a Lakehouse architecture on AWS. If you have any questions, feel free to reach out!
