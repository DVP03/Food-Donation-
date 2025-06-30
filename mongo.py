from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from bson import ObjectId
from typing import List

# ✅ MongoDB Connection (Localhost)
client = MongoClient("mongodb://localhost:27017/")
db = client.feed
collection = db.collection

# ✅ FastAPI App
app = FastAPI()

# ✅ Pydantic model for validation
class User(BaseModel):
    Username: str
    Password: str

#  Push a user (Insert)
@app.post("/users/", response_model=dict)
def add_user(user: User):
    # Check for duplicate Username
    if collection.find_one({"Username": user.Username}):
        raise HTTPException(status_code=400, detail="User already exists")

    result = collection.insert_one(user.dict())
    return {"message": "User added successfully", "id": str(result.inserted_id)}

#  Get all users (Read)
@app.get("/users/", response_model=List[User])
def get_users():
    users = list(collection.find({}, {"_id": 0}))
    return users

#  Delete a user by Username
@app.delete("/users/{username}", response_model=dict)
def delete_user(username: str):
    result = collection.delete_one({"Username": username})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}

#  Delete all users (Optional - for testing)
@app.delete("/users/", response_model=dict)
def delete_all_users():
    result = collection.delete_many({})
    return {"message": f"Deleted {result.deleted_count} users"}
