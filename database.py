from pymongo import MongoClient
from datetime import datetime

MONGO_URI = "mongodb+srv://sociotrace_user:sociotrace123@cluster0.bnj83ko.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URI)

db = client["sociotrace"]
scans_collection = db["scans"]


def save_full_scan(input_url, username, platform, platform_data, sherlock_data):
    document = {
        "searched_username": username,
        "input_url": input_url,
        "platform_detected": platform,
        "platform_data": platform_data,
        "cross_platform_data": sherlock_data,
        "timestamp": datetime.utcnow()
    }

    result = scans_collection.insert_one(document)
    print("Saved to MongoDB with ID:", result.inserted_id)