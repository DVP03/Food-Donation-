
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson.objectid import ObjectId
from typing import List

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.feed
collection = db.collection

app = FastAPI()

# Define the data model
class User(BaseModel):
    Username: str
    Password: str

# Create: Add a new user
@app.post("/users/")
def create_user(user: User):
    if collection.find_one({"Username": user.Username}):
        raise HTTPException(status_code=400, detail="User already exists")
    result = collection.insert_one(user.dict())
    return {"message": "User added", "id": str(result.inserted_id)}

# Read: Get all users
@app.get("/users/", response_model=List[User])
def get_users():
    users = list(collection.find({}, {"_id": 0}))
    return users

# Delete: Delete a user by Username
@app.delete("/users/{username}")
def delete_user(username: str):
    result = collection.delete_one({"Username": username})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}

# Optional: Delete all users (for testing)
@app.delete("/users/")
def delete_all_users():
    result = collection.delete_many({})
    return {"message": f"Deleted {result.deleted_count} users"}
