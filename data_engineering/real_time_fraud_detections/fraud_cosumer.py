from kafka import KafkaConsumer
import json
from fraud_database import init_db, store_transaction

# Initialize the database
init_db()

# Set up Kafka consumer
consumer = KafkaConsumer(
    'transaction-events',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

print("Listening for transactions...")

for message in consumer:
    transaction = message.value
    print(f"Received: {transaction}")
    
    # Store transaction in the database
    store_transaction(transaction)
