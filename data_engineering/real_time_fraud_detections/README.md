## Real-Time Fraud Detection Project Details

### **Project Overview**
This project simulates an **AWS-based real-time fraud detection pipeline** using **Apache Kafka** for event streaming, **Python** for data processing, and **Streamlit** for visualization. In a production environment, this system could leverage **AWS MSK (Managed Streaming for Apache Kafka), AWS Lambda, DynamoDB, and SageMaker** for fraud detection.

### **Technologies Used**
- **Apache Kafka** – Real-time data streaming
- **Python Kafka Producer** – Generates and sends simulated transaction data
- **Python Kafka Consumer** – Processes, detects fraud, and stores transactions
- **SQLite (Simulated Database)** – Stores transactions (In AWS, this could be DynamoDB or RDS)
- **Streamlit Dashboard** – Visualizes fraud transactions in real-time
- **Docker** – Runs Kafka and Zookeeper services

### **Project Structure**
```
real_time_fraud_detections/
├── fraud_transaction_dataset.py  # Kafka Producer (Generates Transactions)
├── fraud_consumer.py             # Kafka Consumer (Processes Transactions & Stores in DB)
├── fraud_database.py             # SQLite Database Logic
├── fraud_dashboard.py            # Streamlit Dashboard for Visualization
├── requirements.txt              # Dependencies
└── README.md                     # Project Documentation
```

### **Setup & Installation**
#### **1. Clone the Repository**
```sh
cd /workspaces/flucas.io/data_engineering/
git clone https://github.com/yourusername/real_time_fraud_detections.git
cd real_time_fraud_detections
```

#### **2. Install Dependencies**
```sh
pip install -r requirements.txt
```

#### **3. Start Kafka & Zookeeper**
```sh
docker-compose up -d
```
Verify Kafka is running:
```sh
docker ps
```

### **Running the Project**
#### **1. Start the Transaction Producer** (Generates Fake Transactions)
```sh
python fraud_transaction_dataset.py
```
Expected output:
```json
{
  "transaction_id": "123e4567-e89b-12d3-a456-426614174000",
  "user_id": 4589,
  "amount": 125.50,
  "is_fraud": 0
}
```

#### **2. Start the Consumer** (Processes & Stores Transactions in Database)
```sh
python fraud_consumer.py
```
Expected output:
```
Listening for transactions...
Received: { transaction details... }
Stored transaction: 123e4567-e89b-12d3-a456-426614174000
```

#### **3. Run the Dashboard** (Visualizes Transactions in Real-Time)
```sh
streamlit run fraud_dashboard.py
```
Now, open [http://localhost:8501](http://localhost:8501) in your browser.

### **Future Enhancements**
Although this project runs locally, it is designed to simulate a **real-time fraud detection system** using AWS services:
- **Kafka → AWS MSK** (Managed Kafka for scalability)
- **SQLite → Amazon DynamoDB or RDS (PostgreSQL)**
- **Streamlit Dashboard → AWS Lambda + API Gateway + QuickSight**
- **Python Consumer → AWS Lambda or EMR** (for scalable fraud detection processing)
- **Future ML Model → AWS SageMaker** for real-time fraud classification

**Next Steps:**
- Integrate **PostgreSQL or MongoDB** instead of SQLite for scalability
- Train a **Machine Learning Model** to classify fraud dynamically
- Deploy on **AWS** using MSK, Lambda, and SageMaker
- Implement **real-time fraud alerts** via AWS SNS, Twilio, or WebSockets

---

## Contact & Collaboration
I’m always open to discussing **data projects, collaboration opportunities, and best practices**. Feel free to explore my projects, review the code, and reach out!

