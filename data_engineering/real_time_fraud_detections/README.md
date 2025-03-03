# 🚀 Real-Time Fraud Detection with Kafka & Python

## 📌 Project Overview
This project demonstrates a **real-time fraud detection system** using:
✅ **Apache Kafka** for real-time data streaming.  
✅ **Python Kafka Producer** to generate simulated transaction data.  
✅ **Python Kafka Consumer** to process and store transactions.  
✅ **SQLite** as a simple database for transaction storage.  
✅ **Streamlit Dashboard** for real-time visualization of fraud transactions.  

---

## 🎯 **Project Structure**
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
✅ Integrate **PostgreSQL** or **MongoDB** instead of SQLite.  
✅ Train a **Machine Learning Model** to classify fraud transactions dynamically.  
✅ Implement **real-time fraud alerts** via AWS Lambda, Twilio, or WebSockets.  

---

## 📩 **Contributing & Contact**
Feel free to fork, contribute, or reach out if you have ideas to enhance this project! 🚀🔥  

