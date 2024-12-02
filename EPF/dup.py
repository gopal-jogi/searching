import json
from pymongo import MongoClient
import random
import string
import uuid

# MongoDB connection
client = MongoClient("mongodb://c8f1423c9e7a4f8d8b4d9d5c3a2b1e6f7d9c0e2f1d3a4b5c6d7e8f9a0b1c2d3e:e4f8a6b9d7c2a1b3c5d6e9f7a8b0c1d4e2f3a5b7c8d9e0f1a6b7c4d3e5f8g7h2@10.128.0.4:27017/admin")  # Replace with your connection string
db = client["EPF"]  # Replace with your database name# Replace with your collection name
error_collection = db["error_col"]  # Replace with your collection name

# Function to generate sample data
def generate_32bit_record_id():
    return uuid.uuid4().int & (1 << 32) - 1  # Truncate UUID to 32 bits

# Function to generate a 3-character combination
def generate_combination():
    return ''.join(random.choices(string.ascii_uppercase, k=4))  # Random 3 uppercase letters

# Simulate errors
def simulate_error():
    error_types = ["CAPTCHA failed", "HTTP 404 Not Found", "HTTP 429 Too Many Requests", "HTTP 500 Internal Server Error"]
    return random.choice(error_types)

# Log errors with 32-bit record_id and 3-character combination
total_errors = 1593  # Number of errors to log
batch_size = 1000

try:
    for start in range(0, total_errors, batch_size):
        errors = []
        for _ in range(batch_size):
            record_id = generate_32bit_record_id()
            combination = generate_combination()
            error = {
                "_id": record_id,  # 32-bit unique identifier
                "error_type": simulate_error(),
                "combination": combination  # Store the combination separately for querying
            }
            errors.append(error)
        
        # Insert errors into the error_logs collection
        if errors:
            error_collection.insert_many(errors)
            print(f"Logged errors for batch starting at record {start + 1}")

except Exception as e:
    print(f"An error occurred: {e}")
