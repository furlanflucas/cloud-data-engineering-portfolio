# 🚀 Real-Time Fraud Detection with Kafka & Python  

## 📌 Project Overview  
This project **simulates an AWS-based real-time fraud detection pipeline** using **Apache Kafka for event streaming**, **Python for data processing**, and **Streamlit for visualization**. In a production environment, this system could leverage **AWS MSK (Managed Streaming for Apache Kafka), AWS Lambda, DynamoDB, and SageMaker** for fraud detection.

## ✅ Technologies Used  
- **Apache Kafka** – Real-time data streaming  
- **Python Kafka Producer** – Generates and sends simulated transaction data  
- **Python Kafka Consumer** – Processes, detects fraud, and stores transactions  
- **SQLite (Simulated Database)** – Stores transactions (In AWS, this could be DynamoDB or RDS)  
- **Streamlit Dashboard** – Visualizes fraud transactions in real-time  
- **Docker** – Runs Kafka and Zookeeper services  

---

## 📂 Project Structure  

📁 `real_time_fraud_detections/`  
├── 📄 `fraud_transaction_dataset.py` → **Kafka Producer (Generates Transactions)**  
├── 📄 `fraud_cosumer.py` → **Kafka Consumer (Processes Transactions & Stores in DB)**  
├── 📄 `fraud_database.py` → **SQLite Database Logic**  
├── 📄 `fraud_dashboard.py` → **Streamlit Dashboard for Visualization**  
├── 📄 `requirements.txt` → **Dependencies**  
└── 📄 `README.md` → **Project Documentation**  

---

## ⚡ **Setup & Installation**

### 1️⃣ **Clone the Repository**
```bash
cd /workspaces/flucas.io/data_engineering/
git clone https://github.com/yourusername/real_time_fraud_detections.git
cd real_time_fraud_detections
```

### 2️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 3️⃣ **Start Kafka & Zookeeper**
```bash
docker-compose up -d
```
Verify Kafka is running:
```bash
docker ps
```

---

## 🚀 **Running the Project**
### 1️⃣ **Start the Transaction Producer** (Generates Fake Transactions)
```bash
python fraud_transaction_dataset.py
```
✔ Expected output:
```
Sent: { "transaction_id": "123e4567-e89b-12d3-a456-426614174000", "user_id": 4589, "amount": 125.50, "is_fraud": 0 }
```

### 2️⃣ **Start the Consumer** (Processes & Stores Transactions in Database)
```bash
python fraud_cosumer.py
```
✔ Expected output:
```
Listening for transactions...
Received: { "transaction_id": "123e4567-e89b-12d3-a456-426614174000", "user_id": 4589, "amount": 125.50, "is_fraud": 0 }
Stored transaction: 123e4567-e89b-12d3-a456-426614174000
```

### 3️⃣ **Run the Dashboard** (Visualizes Transactions in Real-Time)
```bash
streamlit run fraud_dashboard.py
```
✔ Open your browser and go to: `http://localhost:8501`

---

## 🛠 **Kafka Manual Testing (Optional)**

### **List Topics**
```bash
docker exec -it kafka /home/appuser/kafka/bin/kafka-topics.sh --list --bootstrap-server kafka:9092
```

### **Manually Send a Test Message**
```bash
docker exec -it kafka /home/appuser/kafka/bin/kafka-console-producer.sh --broker-list kafka:9092 --topic transaction-events
```
Then enter:
```json
{"transaction_id":"test123","user_id":9999,"amount":2500.00, "is_fraud":1}
```

### **Consume Messages**
```bash
docker exec -it kafka /home/appuser/kafka/bin/kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic transaction-events --from-beginning
```
✔ Expected output:
```json
{"transaction_id":"test123","user_id":9999,"amount":2500.00, "is_fraud":1}
```

---

## 📌 **Future Enhancements**
📌 AWS Simulation & Future Enhancements
Although this project runs locally, it is designed to simulate a real-time fraud detection system that would use AWS services:

- **✅ Kafka → AWS MSK** (Managed Kafka for scalability)
- **✅ SQLite → Amazon DynamoDB or RDS** (PostgreSQL)
- **✅ Streamlit Dashboard → AWS Lambda + API Gateway + QuickSight**
- **✅ Python Consumer → AWS Lambda or EMR** (for scalable fraud detection processing)
- **✅ Future ML Model → AWS SageMaker for real-time fraud classification**

Next Steps:
- **🔹 Integrate PostgreSQL or MongoDB instead of SQLite for scalability**
- **🔹 Train a Machine Learning Model to classify fraud dynamically**
- **🔹 Deploy on AWS using MSK, Lambda, and SageMaker**
- **🔹 Implement real-time fraud alerts via AWS SNS, Twilio, or WebSockets**


---

## 📩 **Contributing & Contact**
Feel free to fork, contribute, or reach out if you have ideas to enhance this project! 🚀🔥  

