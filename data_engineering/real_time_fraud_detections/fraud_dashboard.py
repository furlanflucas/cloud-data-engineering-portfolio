import streamlit as st
import pandas as pd
import sqlite3

st.title("Real-Time Fraud Detection Dashboard")

# Load transactions from database
conn = sqlite3.connect("fraud_detection.db")
df = pd.read_sql("SELECT * FROM transactions ORDER BY timestamp DESC LIMIT 10", conn)
conn.close()

st.dataframe(df)
