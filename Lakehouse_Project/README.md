# STEDI Lakehouse Solution

## Project Overview

This project implements a **Lakehouse architecture** using **AWS Glue, S3, Python, and Apache Spark** to process IoT data for **STEDI**. The goal is to clean, transform, and integrate customer, accelerometer, and step trainer data to support data science and machine learning initiatives.

## Tech Stack
- **AWS Glue** (ETL processing)
- **Amazon S3** (Data Lake storage)
- **Apache Spark** (Distributed processing)
- **Amazon Athena** (SQL queries on S3 data)
- **Python** (Glue Job scripting)
- **IAM Roles** (Access control)

## Data Pipeline Workflow

1. **Setup S3 Buckets**
   - `customer–bucket/`
   - `accelerometer--bucket/`
   - `step_trainer–bucket/`

2. **Landing Zone** (Raw data ingestion in S3)
   - `customer_landing_folder/`
   - `accelerometer_landing_folder/`
   - `step_trainer_landing_folder/`
   
3. **Trusted Zone** (Data cleaning & filtering)
   - `customer_trusted/`: Only customers who agreed to share data.
   - `accelerometer_trusted/`: Only accelerometer data from customers who opted in.
   - `step_trainer_trusted/`: Only step trainer data for opted-in customers.
   
4. **Curated Zone** (Refined dataset for ML models)
   - `customers_curated/`: Customers with accelerometer data.
   - `machine_learning_curated/`: Merged dataset with step trainer & accelerometer readings.

## AWS Glue Jobs
| Job Name | Description |
|----------|-------------|
| **Customer Trusted** | Filters customers who agreed to share data. |
| **Accelerometer Trusted** | Filters accelerometer data for opted-in customers. |
| **Step Trainer Trusted** | Filters step trainer data for opted-in customers. |
| **Customers Curated** | Includes only customers with accelerometer data. |
| **Machine Learning Curated** | Joins accelerometer and step trainer data for ML. |

## SQL Queries
### **Step 5: Creating `step_trainer_trusted`**
```sql
SELECT s.* 
FROM step_trainer_landing s
WHERE s.serialnumber IN (
    SELECT DISTINCT c.serialnumber
    FROM customer_curated c
);
```
### **Step 6: Creating `machine_learning_curated`**
```sql
SELECT 
    a.user AS customer_id,
    a.timestamp AS accelerometer_timestamp,
    a.x AS accelerometer_x,
    a.y AS accelerometer_y,
    a.z AS accelerometer_z,
    s.sensorreadingtime AS step_trainer_timestamp,
    s.distancefromobject AS step_trainer_distance
FROM accelerometer_trusted a
JOIN step_trainer_trusted s
ON a.timestamp = s.sensorreadingtime;
```

## Verification Steps
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

## Troubleshooting
### **403 Access Denied Errors in Glue Jobs**
1. Ensure **IAM Role (`AWSGlueServiceRole`)** has `s3:PutObject` permission:
   ```bash
   aws iam put-role-policy \
       --role-name AWSGlueServiceRole \
       --policy-name GlueS3AccessPolicy \
       --policy-document '{
           "Version": "2012-10-17",
           "Statement": [
               {
                   "Effect": "Allow",
                   "Action": [
                       "s3:PutObject", "s3:GetObject", "s3:ListBucket"
                   ],
                   "Resource": [
                       "arn:aws:s3:::your-bucket-name",
                       "arn:aws:s3:::your-bucket-name/*"
                   ]
               }
           ]
       }'
   ```
2. Ensure **Glue job script** has `partitionKeys: []` to avoid appending data incorrectly.
3. Delete **old S3 data** before rerunning jobs:
   ```bash
   aws s3 rm s3://your-bucket/machine_learning_curated/ --recursive
   ```
4. Refresh **Athena Metadata**:
   ```sql
   MSCK REPAIR TABLE machine_learning_curated;
   ```

## Deliverables
- AWS Glue **Job Scripts** (Python)
- Athena **Query Screenshots**
- S3 **Raw & Processed Data**
- README Documentation

## Future Enhancements
- Implement **AWS Step Functions** for automated pipeline orchestration.
- Integrate **AWS Glue Data Catalog** for schema enforcement.
- Optimize query performance using **S3 partitioning**.

## Author
This project was created as part of a data engineering workflow to build a Lakehouse architecture on AWS. If you have any questions, feel free to reach out!

