import sqlite3

# Initialize the SQLite database
def init_db():
    conn = sqlite3.connect("fraud_detection.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
        transaction_id TEXT PRIMARY KEY,
        user_id INT,
        amount REAL,
        timestamp TEXT,
        merchant_category TEXT,
        location TEXT,
        payment_method TEXT,
        is_fraud INT
    )''')

    conn.commit()
    conn.close()

# Insert transactions into the database
def store_transaction(transaction):
    conn = sqlite3.connect("fraud_detection.db")
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO transactions VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (
        transaction["transaction_id"],
        transaction["user_id"],
        transaction["amount"],
        transaction["timestamp"],
        transaction["merchant_category"],
        transaction["location"],
        transaction["payment_method"],
        transaction["is_fraud"]
    ))

    conn.commit()
    conn.close()
